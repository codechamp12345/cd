import socket

c = socket.socket()
c.connect(("localhost", 9999))

while True:
    print("\n1. Read\n2. Write\n3. Delete\n4. Exit")
    ch = input("Enter your choice: ")

    if ch == "1":
        key = input("Enter key to read: ")
        c.send(f"READ {key}".encode())

    elif ch == "2":
        key = input("Enter key to write: ")
        val = input("Enter value: ")
        c.send(f"WRITE {key} {val}".encode())

    elif ch == "3":
        key = input("Enter key to delete: ")
        c.send(f"DELETE {key}".encode())

    elif ch == "4":
        break

    else:
        print("Invalid choice")
        continue

    print("Server response:", c.recv(1024).decode())

c.close()