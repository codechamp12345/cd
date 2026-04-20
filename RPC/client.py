import socket

c = socket.socket()
c.connect(("localhost", 5000))

print("Enter: number operator number (example: 5 + 3)")

while True:
    exp = input("Enter: ")

    if exp == "bye":
        break

    c.send(exp.encode())
    result = c.recv(1024).decode()
    print("Result:", result)

c.close()