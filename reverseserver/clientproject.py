import socket
s = socket.socket()
s.connect(('localhost', 1488))
st = raw_input()
s.send(st)

data = s.recv(1024)
s.close()
print data