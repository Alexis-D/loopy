# loopy

A toy event loop to get a better grasp of how [`asyncio`](https://docs.python.org/3/library/asyncio.html) works behind
the scenes. It relies on [`selectors`](https://docs.python.org/3/library/selectors.html) for the socket I/O.

In one shell, run the toy program with: `rye run loopy`, in other shells, send data to the server using
`socat - TCP:localhost:1234`.

Output will be something like this:

```
2024-07-26 12:11:58 [info     ] Count                          i=0
2024-07-26 12:11:59 [info     ] Count                          i=1
2024-07-26 12:12:00 [info     ] Count                          i=2
2024-07-26 12:12:01 [info     ] Count                          i=3
2024-07-26 12:12:02 [info     ] Count                          i=4
2024-07-26 12:12:03 [info     ] Count                          i=5
2024-07-26 12:12:04 [info     ] Count                          i=6
2024-07-26 12:12:05 [info     ] Count                          i=7
2024-07-26 12:12:06 [info     ] Count                          i=8
2024-07-26 12:12:07 [info     ] Count                          i=9
2024-07-26 12:12:08 [info     ] Count                          i=10
2024-07-26 12:12:09 [info     ] Count                          i=11
2024-07-26 12:12:10 [info     ] Count                          i=12
2024-07-26 12:12:11 [info     ] Count                          i=13
2024-07-26 12:12:12 [info     ] Count                          i=14
2024-07-26 12:12:12 [info     ] Accept                         from_=('127.0.0.1', 56776)
2024-07-26 12:12:13 [info     ] Count                          i=15
2024-07-26 12:12:14 [info     ] Count                          i=16
2024-07-26 12:12:14 [info     ] Recvd                          data=b'hello\n' from_=('127.0.0.1', 56776)
2024-07-26 12:12:15 [info     ] Count                          i=17
2024-07-26 12:12:15 [info     ] Recvd                          data=b'world\n' from_=('127.0.0.1', 56776)
2024-07-26 12:12:16 [info     ] Count                          i=18
2024-07-26 12:12:17 [info     ] Count                          i=19
2024-07-26 12:12:17 [info     ] Accept                         from_=('127.0.0.1', 56778)
2024-07-26 12:12:18 [info     ] Count                          i=20
2024-07-26 12:12:19 [info     ] Count                          i=21
2024-07-26 12:12:20 [info     ] Count                          i=22
2024-07-26 12:12:20 [info     ] Recvd                          data=b'bye bye\n' from_=('127.0.0.1', 56778)
2024-07-26 12:12:21 [info     ] Count                          i=23
2024-07-26 12:12:22 [info     ] Count                          i=24
```

As can be seen this all runs on a single thread, and happily interlaces work, whether that printing counts on
a schedule, or reading from various network connections.
