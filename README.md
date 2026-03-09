# TCP Real-Time Sensor & Chat System

## Description
This project demonstrates a multi-threaded TCP client-server communication system. It is designed to simulate a remote hardware sensor (like a temperature probe) while simultaneously allowing manual two-way communication (chat) between the client and server terminals.

### Key Features:
* **Automated Sensor Data**: The client generates a random temperature value (between 20.0°C and 35.0°C) and transmits it to the server every 5 seconds.
* **Multi-Threaded Communication**: Both scripts use the `threading` library to listen for incoming messages and send outgoing data at the same time without blocking.
* **Manual Override**: Users can type custom messages in either terminal to communicate manually.
* **Network Flexible**: Configured to work on `localhost` or over a local network/hotspot via IP binding.

---

## How to Run

### 1. Prerequisites
Ensure you have Python 3.x installed on your system. No external libraries are required as this uses the built-in `socket` and `threading` modules.

### 2. Launch the Server
1. Open a terminal.
2. Navigate to the project folder.
3. Run the server:
   ```bash
   python server.py
