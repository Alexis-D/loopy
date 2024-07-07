# loopy

A toy event loop to get a better grasp of how [`asyncio`](https://docs.python.org/3/library/asyncio.html) works behind
the scenes. It relies on [`selectors`](https://docs.python.org/3/library/selectors.html) for the socket I/O.

In one shell, run the toy program with: `rye run loopy`, in other shells, send data to the server using `socat
- TCP:localhost:1234`.

Output will be something like this:

```
2024-07-07 14:54:55,836 INFO __init__ MainThread Count: 0
2024-07-07 14:54:56,847 INFO __init__ MainThread Count: 1
2024-07-07 14:54:57,856 INFO __init__ MainThread Count: 2
2024-07-07 14:54:58,866 INFO __init__ MainThread Count: 3
2024-07-07 14:54:58,894 INFO __init__ MainThread Accept from ('127.0.0.1', 62857)
2024-07-07 14:54:59,903 INFO __init__ MainThread Count: 4
2024-07-07 14:55:00,256 INFO __init__ MainThread Accept from ('127.0.0.1', 62859)
2024-07-07 14:55:00,963 INFO __init__ MainThread Count: 5
2024-07-07 14:55:01,973 INFO __init__ MainThread Count: 6
2024-07-07 14:55:02,982 INFO __init__ MainThread Count: 7
2024-07-07 14:55:03,992 INFO __init__ MainThread Count: 8
2024-07-07 14:55:05,000 INFO __init__ MainThread Count: 9
2024-07-07 14:55:05,865 INFO __init__ MainThread Recvd (from ('127.0.0.1', 62857)): b'hello from one connection!\n'
2024-07-07 14:55:06,067 INFO __init__ MainThread Count: 10
2024-07-07 14:55:07,076 INFO __init__ MainThread Count: 11
2024-07-07 14:55:08,084 INFO __init__ MainThread Count: 12
2024-07-07 14:55:09,091 INFO __init__ MainThread Count: 13
2024-07-07 14:55:10,101 INFO __init__ MainThread Count: 14
2024-07-07 14:55:11,112 INFO __init__ MainThread Count: 15
2024-07-07 14:55:12,120 INFO __init__ MainThread Count: 16
2024-07-07 14:55:13,128 INFO __init__ MainThread Count: 17
2024-07-07 14:55:14,137 INFO __init__ MainThread Count: 18
2024-07-07 14:55:15,041 INFO __init__ MainThread Recvd (from ('127.0.0.1', 62859)): b'hello from another one!\n'
2024-07-07 14:55:15,143 INFO __init__ MainThread Count: 19
2024-07-07 14:55:16,153 INFO __init__ MainThread Count: 20
2024-07-07 14:55:17,163 INFO __init__ MainThread Count: 21
2024-07-07 14:55:18,172 INFO __init__ MainThread Count: 22
2024-07-07 14:55:18,207 INFO __init__ MainThread Recvd (from ('127.0.0.1', 62857)): b'bye bye!\n'
2024-07-07 14:55:19,219 INFO __init__ MainThread Count: 23
2024-07-07 14:55:20,228 INFO __init__ MainThread Count: 24
2024-07-07 14:55:20,344 INFO __init__ MainThread Recvd (from ('127.0.0.1', 62859)): b'bye bye\n'
2024-07-07 14:55:21,311 INFO __init__ MainThread Count: 25
2024-07-07 14:55:22,408 INFO __init__ MainThread Count: 26
```

As can be seen this all runs on a single thread, and happily interlaces work, whether that printing counts on
a schedule, or reading from various network connections.
