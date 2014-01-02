x = open('numbers.txt', 'r')
print 'Does this do what I think?', x
y = x.readlines()
for thing in y:
	print thing
