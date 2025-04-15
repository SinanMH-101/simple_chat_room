# TCP Chat App

This is a small rpoject to practice some simple networking concepts.A simple multi-user terminal-based chat application built using Python sockets and threading. The project includes a server that accepts multiple client connections and broadcasts messages in real-time.

## What I learned:
- How TCP/IP networking works using sockets
- Difference between server-side and client-side logic
- Managing multiple connections using threads
- How to handle input/output gracefully in a multi-threaded console app
- Debugging common issues like dropped connections or encoding errors
- Unix commands

## Features

- Multiple clients can join the server
- Real-time message broadcasting
- Nickname system for identifying users
- Clean message formatting and improved input experience
- Graceful handling of disconnections and errors



## Technologies Used

| Component     | Technology                        |
|---------------|-----------------------------------|
| Language      | Python 3                          |
| Networking    | `socket` module                   |
| Concurrency   | `threading` module                |
| Terminal UX   | `sys`, `print`, `input`, formatting |

---


## How to Run

1. **Start the server**  
   Open a terminal and run:
   ```bash
   python server.py
   ```

1. **Run the client(s)**  
   In a separate terminal(s), run:
   ```bash
   python client.py
   ```

## Screenshot:
![alt text](<chat_room_screenshot.png>)