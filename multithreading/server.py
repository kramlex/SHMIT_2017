# coding: utf-8
import socket
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf8')	

client_sockets = []


def wait_for_messages(user_socket, nick):
	while True:
		data = user_socket.recv(1024)
		if not data:
			user_socket.close()
			break
		message = nick + ": " + data.decode()
		print message

		for i in client_sockets:
			if i != user_socket:
				i.send('\n'+message)

# settings
sys.stdout.write("Enter server port:")
port = raw_input()
sys.stdout.write("Enter the number of users:")
count_listener = raw_input()

#


host = '172.20.10.2'
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((host, int(port)))
s.listen(int(count_listener))

while True:
	conn, addr = s.accept()
	client_sockets.append(conn)
	nick = conn.recv(1024)
	nick = nick.decode()
	print('Connected by',addr,nick)
	threading.Thread(target=wait_for_messages, args = (conn, nick)).start()
