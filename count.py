x = {'fruit':1, 1:'orange', 2:'ni', 3:'san'}
for thing in x:
	if thing == 'fruit':
		x[thing] = x[thing] + 1
print x
