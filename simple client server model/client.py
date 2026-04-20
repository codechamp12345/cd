import socket

c = socket.socket()
c.connect(("localhost", 5000))

while True:
    msg = input("Client: ")
    c.send(msg.encode())
    
    if msg == "bye":
        break
    
    reply = c.recv(1024).decode()
    print("Server:", reply)

c.close()