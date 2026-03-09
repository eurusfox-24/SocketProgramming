import socket
import time
import random

def start_client():
    # --- CONFIGURATION ---
    # Use '127.0.0.1' for local test
    # Use '172.20.10.3' (your IP) for mobile hotspot test
    server_ip = '127.0.0.1' 
    port = 55555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        print(f"Attempting to connect to {server_ip}...")
        client_socket.connect((server_ip, port))
        print("Connected! Sending sensor data every 5 seconds...")

        while True:
            # Generate random temperature between 20.0 and 30.0
            temp = round(random.uniform(20.0, 30.0), 1)
            message = f"Temperature: {temp} C"
            
            # Send data to server
            client_socket.sendall(message.encode('utf-8'))
            print(f"Sent: {message}")
            
            # Wait for 5 seconds
            time.sleep(5)

    except ConnectionRefusedError:
        print("Error: Could not connect. Is the server running?")
    except KeyboardInterrupt:
        print("\nClient stopped.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
