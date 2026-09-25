# Ch7 — Working with Real-Time Data and Sockets

**Source:** *Python for Algorithmic Trading: From Idea to Cloud Deployment* —
Yves Hilpisch (O'Reilly, 2021)

## Terminology

- **Network socket**: endpoint of a connection (just "socket").
- **Socket address**: IP address + port number.
- **Socket protocol**: e.g. TCP — defines how communication is handled.
- **Socket pair**: the local + remote socket communicating.
- **Socket API**: the programming interface to control sockets.

Deploying a strategy flips the game: data arrives in real time and in
mass, so real-time processing and decision-making are mandatory. Sockets
are the tool of choice.

## ZeroMQ and PUB-SUB

ZeroMQ (pyzmq): a lightweight, fast, scalable socket library with
language wrappers and several patterns. The **publisher-subscriber
(PUB-SUB)** pattern is the natural fit for market data: one socket
publishes, many sockets receive simultaneously (like a radio broadcast).
Application: a central service broadcasts ticks as they arrive; thousands
of subscribers (traders) process them.

Core API:
```python
import zmq
context = zmq.Context()
socket = context.socket(zmq.PUB)          # or zmq.SUB
socket.bind('tcp://0.0.0.0:5555')          # server binds
socket.connect('tcp://<host>:5555')        # client connects
socket.send_string(msg)                    # publish
msg = socket.recv_string()                 # receive
```

## Tick data server & client

- **Server**: simulates tick prices via the exact Euler discretization of
  GBM, `S_t = S_{t−Δt}·exp((r − σ²/2)Δt + σ√Δt·z)`, publishes on a PUB
  socket at randomized intervals (random price path + random wait time).
- **Client**: a SUB socket connects and receives ticks; add a topic filter
  (`socket.setsockopt(zmq.SUBSCRIBE, b'')`) to subscribe to all topics.
- **Signal generation in real time**: the client maintains a rolling
  window (e.g. 20 ticks), computes an SMA, and generates buy/sell signals
  as new ticks arrive — the online version of the SMA strategy.
- **Visualization**: Plotly renders streaming data in real time (dash-style
  updating charts) — live curves of price and signals.

## Practical notes

- Runs require two+ processes at once: server in one terminal, client in
  another (or a Notebook) — sockets bind ports that both sides share.
- Port choice matters; keep server and client on the same port/protocol.
- Unencrypted sockets send plaintext — a security risk in production
  (encrypt or use a VPN/tunnel for real deployments).

## Key takeaways

- PUB-SUB is the canonical pattern for streaming market data: one
  publisher, many subscribers; ZeroMQ makes it a few lines of code.
- The Euler GBM tick simulator is the standard stand-in for live prices in
  development.
- Real-time signal generation = rolling window + threshold, applied to
  each incoming tick (the online analog of vectorized signals).
- Run server and client as separate processes; mind ports, topics, and
  the plaintext-security caveat before going live.
