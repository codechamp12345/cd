import socket, threading

mem = {}

def handle(c, addr):
    print(f"Connection established with {addr}")
    
    while True:
        req = c.recv(1024).decode()
        if not req:
            break
        
        print(f"Received from {addr}: {req}")
        parts = req.split()

        if parts[0] == "WRITE":
            mem[parts[1]] = parts[2]
            res = "OK"

        elif parts[0] == "READ":
            val = mem.get(parts[1], "Not Found")
            res = f"OK {val}"

        elif parts[0] == "DELETE":
            if parts[1] in mem:
                del mem[parts[1]]
                res = "OK"
            else:
                res = "Not Found"

        else:
            res = "Invalid"

        c.send(res.encode())

    print(f"Client {addr} disconnected")
    c.close()
    print(f"Connection with {addr} closed")


s = socket.socket()
s.bind(("localhost", 9999))
s.listen(5)

print("Distributed Shared Memory Server started on port 9999...")

while True:
    c, addr = s.accept()
    print(f"Accepted connection from {addr}")
    threading.Thread(target=handle, args=(c, addr)).start()