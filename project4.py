a = raw_input().split()
v = {}
for i in range(len(a)):
	a[i] = list(a[i])
	a[i].sort()
	a[i] = ''.join( a[i] )
	m = v.get(str(a[i]),0)
	if m == 0:
		v[str(a[i])] = 1
	else:
		v[str(a[i])] += 1
print v
