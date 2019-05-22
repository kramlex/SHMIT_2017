import threading
from time import sleep

def print_n(n):
	while True:
		print(n)
		sleep(n)


t1 = threading.Thread(target = print_n , args=([1]))
t2 = threading.Thread(target = print_n , args =([2])) 
t3 = threading.Thread(target = print_n , args =([3])) 
t1.start()
t2.start()
t3.start()
t1.join()
