import threading
import socket
import sys

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))


print_lock = threading.Lock()

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                with print_lock:
                    sys.stdout.write('\r' + ' ' * 80 + '\r')  # clear current line
                    print(f'\n{message}\n> ', end='', flush=True)
        except:
            print("\nConnection closed or an error occurred.")
            client.close()
            break

def write():
    while True:
        try:
            while True:
                message = input("> ")
                full_message = f'{nickname}: {message}'
                client.send(full_message.encode('ascii'))
        except:
            print("Failed to send message.")
            client.close()
            break

receive_thread = threading.Thread(target=receive, daemon=True)
receive_thread.start()

write_thread = threading.Thread(target=write, daemon=True)
write_thread.start()

receive_thread.join()
write_thread.join()
