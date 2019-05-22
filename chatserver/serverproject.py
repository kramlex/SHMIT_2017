# -*- coding: utf-8 -*-

import socket
import sys
import random
import codecs
import locale

host = '172.20.10.2'
port = 14888
s = socket.socket(
			socket.AF_INET , socket.SOCK_STREAM)
s.bind((host, port))	
s.listen(2)
sys.stdout.write("Enter your name: ")
name = raw_input()
print "Your name: " + name
ckey = random.randint(1,5)
conn, addr = s.accept()
print('Connect by',addr)
conn.send(str(ckey).encode())
while True:
	data = conn.recv(1024)
	data1 = ''
	for i in data:
		data1 += chr(ord(i)-ckey)
	print ('\n' + data1.decode('ascii'))
	sys.stdout.write(name +": ")
	answer = name + ": " + raw_input() + "\n"
	answer1 = ''
	for i in answer:
		answer1 += chr(ord(i)+ckey)
	
	conn.send(answer1.encode())
conn.sendall(data)
conn.close()