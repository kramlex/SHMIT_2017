import socket
import sys
import threading

client_sockets = []
#function

def wait_for_messages(user_socket):
	while True:
		data = user_socket.recv(2048)
		if not data:
			user_socket.close()
			break
		#allsend(data)
		#print data
		for i in client_sockets:
		 	if i != user_socket:
				i.send(data)

				

#

# settings
sys.stdout.write("Enter server port:")
port = raw_input()
sys.stdout.write("Enter the number of users:")
count_listener = raw_input()
host = '172.20.10.3'
#

#install settings
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((host, int(port)))
s.listen(int(count_listener))
#

while True:
	conn, addr = s.accept()
	client_sockets.append(conn)
	print('Connected by',addr)
	threading.Thread(target=wait_for_messages, args = (conn, )).start()
