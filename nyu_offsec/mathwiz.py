import socket
import sys

# create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connection info
server_address = ('offsec-chalbroker.osiris.cyber.nyu.edu', 1236)
# connect to the server
sock.connect(server_address)

try:
	# receive data from the server
    print(sock.recv(1024))
    # tell the server who you are
    sock.send(b"jd3846\n") # your net id
	# receive confirmation from the server
    print(sock.recv(1024))

	# receive the challenge
    data = sock.recv(1024).decode("utf8")
    print(data)

    print(data.find("??"))
    eq = data.find("=")
    start = 183
    ls = data[183:193].split(" ")
    print(ls)
    op = ls[1]
    n1 = int(ls[0])
    n2 = int(ls[2])

    if op == '+':
        ret = n1 + n2
    elif op == '-':
        ret = n1 - n2
    elif op == '*':
        ret = n1 * n2
    elif ret == '/':
        ret = n1 / n2

    ret = str(ret).encode('utf-8')

	#
	# Solve the given challenge and return the answer as specified by the instructions
	#

	# send the server your answer
    print(ret)
    sock.send(ret)
    data = sock.recv(1024)
    print(data)

finally:
	# close the connection
    sock.close()