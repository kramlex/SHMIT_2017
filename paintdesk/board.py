import pygame
import threading
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.20.10.3', 14888))
pygame.init()
screen = pygame.display.set_mode([1280, 720])

Finished = False
Drawing = False
Erase = False
ErsAll = False
k = 0
screen.fill([224, 224, 224])
def wait():
	while True:
		data = s.recv(2048)
		data = data.decode()
		print data
		l = data.split()

		if len(l) >= 5:
			if (l[2] != 'False' and l[2] != 'True') or len(l)%5 != 0:
				print ('\n All Bad \n')
				continue


			if l[2] == 'False':
					color = [0,0,0]
					rad = 2
			else:
				color = [224, 224, 224]
				rad = 15
				
			pygame.draw.circle(screen, color, [int(l[0]), int(l[1])], rad)
			if l[3] == '1' and l[4] == pip:
				pygame.draw.line(screen, color, [int(l[0]), int(l[1])], l1, rad*2)
			l1 = []
			l1.append(int(l[0]))
			l1.append(int(l[1]))
			pip = l[4]


threading.Thread(target = wait).start()

while True:

	pygame.draw.rect(screen, [64, 64, 64], [0, 0, 1280, 720], 15)
	if Drawing == True:
		pos = pygame.mouse.get_pos()
		mx, my = pos[0], pos[1]

		if Erase == False:
			color = [0,0,0]
			rad = 2
		else:
			color = [224, 224, 224]
			rad = 15
		
		pygame.draw.circle(screen, color, [mx, my], rad)
		if k == 1:
			pygame.draw.line(screen, color, pos, pos1, rad*2)
		
		mess = []
		pos2 = []
		pos2.append(str(pos[0]) + ' ')
		pos2.append(str(pos[1]) + ' ')
		stpos = ''.join(pos2)
		mess.append(stpos)
		mess.append(str(Erase) + ' ')
		mess.append(str(k) + ' ')
		mess.append(socket.gethostname() + ' ')
		st = ''.join(mess)
		s.send(st.encode())

		k = 1
		pos1 = pos


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Finished = True
			break

		if event.type == pygame.MOUSEBUTTONDOWN:
			Drawing = True
			if event.button == 3:
				Erase = True
		
		if event.type == pygame.MOUSEBUTTONUP:
			Drawing = False
			k = 0
			if event.button == 3:
				Erase = False


	if Finished == True:
		break

	pygame.display.flip()
