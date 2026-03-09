import socket
import threading

def receive_messages(conn):
    """Function to constantly listen for data from the client."""
    while True:
        try:
            message = conn.recv(1024).decode('utf-8')
            if not message:
                print("\n[Client disconnected]")
                break
            print(f"\n[CLIENT]: {message}")
            print("[YOU]: ", end="") # Keep the prompt visible
        except:
            break

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Listen on all interfaces so 172.20.10.3 is active
    host = '0.0.0.0'
    port = 55555
    
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server started on {host}:{port}. Waiting for connection...")

    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    # Start a background thread to receive messages
    threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()

    # Main loop to send messages from the terminal
    while True:
        msg = input("[YOU]: ")
        if msg.lower() == 'exit':
            break
        try:
            conn.sendall(msg.encode('utf-8'))
        except:
            print("Connection lost.")
            break

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
