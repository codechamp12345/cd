import socket

s = socket.socket()
s.bind(("localhost", 5000))
s.listen(1)

print("Waiting...")
conn, addr = s.accept()
print("Connected")

while True:
    msg = conn.recv(1024).decode()
    print("Client:", msg)
    
    if msg == "bye":
        break
    
    reply = input("Server: ")
    conn.send(reply.encode())

conn.close()