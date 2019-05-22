import socket


host = ""
port = 1488
s = socket.socket(
			socket.AF_INET , socket.SOCK_STREAM)

s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connect by',addr)
while True:
	data = conn.recv(1024)
	s = list(data)
	s.reverse()
	data = ''.join(s)
	if not data: break
	conn.sendall(data)
conn.close()
