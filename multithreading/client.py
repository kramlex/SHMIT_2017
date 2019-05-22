import socket
import threading
import sys
reload(sys)
sys.setdefaultencoding('utf8')	

# settings
sys.stdout.write("Enter Server-IP: ")
host = raw_input()
sys.stdout.write("Enter Server-Port: ")
port = int(raw_input())
#

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.connect((host , port))
def wait_for_messages():
	while True:
		data = s.recv(1024)
		data = data.decode()
		print data

threading.Thread(target=wait_for_messages).start()

print("Connected to server: " + host + ":" + str(port))

sys.stdout.write("Enter your name: ")
name = raw_input()
s.send(name)

while True:
	answer = raw_input(name + ": ")
	s.send(answer.encode())