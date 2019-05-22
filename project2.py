a = raw_input()
a = a.split()
b = {}
for i in a:	
	m = b.get(i,0)
	if m == 0:
		b[i] = 1
	else:
		b[i] += 1
for i in range(len(b)):
	print str(b.keys()[i]) + " " + str(b[b.keys()[i]])
	
 