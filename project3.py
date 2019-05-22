a = raw_input().split()
b = {}
for i in range(0,len(a),2):
	m = b.get(a[i],a[i+1])
	if m == a[i+1]:
		b[a[i]] = a[i+1]
	else:
		if a[i+1] < b[a[i]]:
			b[a[i]] = a[i+1]
			
for i in range(len(b)):
	print str(b.keys()[i]) + " " + str(b[b.keys()[i]])