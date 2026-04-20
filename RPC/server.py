import socket

s = socket.socket()
s.bind(("localhost", 5000))
s.listen(1)

print("Server started")
c, addr = s.accept()

while True:
    data = c.recv(1024).decode()
    if not data:
        break

    try:
        data = data.replace(" ", "")  # remove spaces

        n1 = int(data[0])
        op = data[1]
        n2 = int(data[2])

        if op == '+':
            res = n1 + n2
        elif op == '-':
            res = n1 - n2
        elif op == '*':
            res = n1 * n2
        elif op == '/':
            res = n1 / n2 if n2 != 0 else "Error"
        else:
            res = "Invalid"

    except:
        res = "Invalid Input"

    c.send(str(res).encode())

c.close()