import functools
import heapq
import logging
import selectors
import socket
import time
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class _Task:
    priority: int
    callback: Any = field(compare=False)


class EventLoop:
    def __init__(self):
        self._tasks = []
        self._sel = selectors.DefaultSelector()

    def call_soon(self, fn):
        """Used to schedule a function that is ready to fun"""
        heapq.heappush(self._tasks, _Task(0, fn))

    def call_later(self, fn, delay_seconds):
        """Used to schedule a function in the future"""
        priority = time.monotonic() + delay_seconds
        heapq.heappush(self._tasks, _Task(priority, fn))

    def call_when_ready_to_read(self, fileobj, fn):
        """When fileobj becomes readable, fn will be called -with fileobj- as an argument"""
        self._sel.register(
            fileobj, selectors.EVENT_READ, data=functools.partial(fn, fileobj)
        )

    def forget(self, fileobj):
        """Used to stop monitoring fileobj"""
        self._sel.unregister(fileobj)

    def run_forever(self):
        while True:
            timeout = 0.1

            while self._tasks:
                # as long as we have task, look at the head task
                task = heapq.heappop(self._tasks)

                if task.priority == 0 or task.priority < time.monotonic():
                    # if it can be executed immediately, execute it
                    task.callback()
                else:
                    # otherwise queue it back, we can't run any more tasks immediately
                    heapq.heappush(self._tasks, task)
                    timeout = min(timeout, task.priority - time.monotonic())
                    break

            # we don't have ready tasks, let's see if any fd is ready to be read from
            for key, _ in self._sel.select(0.1):
                # schedule the callback
                self.call_soon(key.data)


def count(loop, i=0):
    logging.info(f"Count: {i}")
    loop.call_later(functools.partial(count, loop, i + 1), 1)


def read(loop, addr, conn):
    data = conn.recv(128)

    if data:
        logging.info(f"Recvd (from {addr}): {data!r}")
    else:
        loop.forget(conn)
        conn.close()


def accept(loop, sock):
    conn, addr = sock.accept()
    logging.info(f"Accept from {addr}")
    conn.setblocking(False)

    loop.call_when_ready_to_read(conn, functools.partial(read, loop, addr))


def start_server(loop):
    sock = socket.socket()
    sock.bind(("localhost", 1234))
    sock.listen()
    sock.setblocking(False)

    loop.call_when_ready_to_read(sock, functools.partial(accept, loop))


def main():
    logging.basicConfig(
        format="%(asctime)s %(levelname)s %(module)s %(threadName)s %(message)s",
        level=logging.INFO,
    )

    loop = EventLoop()
    loop.call_soon(functools.partial(count, loop))
    loop.call_soon(functools.partial(start_server, loop))
    loop.run_forever()
