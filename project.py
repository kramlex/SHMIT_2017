for a in range(1001):
	if a % 3 == 0 and a % 5 != 0:
		print str(a) + " fizz"
	elif a % 5 == 0 and a % 3 != 0:
		print str(a) + " bazz"
	elif a % 5 == 0 and a % 3 == 0:
		print str(a) + " fizzbazz"