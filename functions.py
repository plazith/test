def sq(arg):
	return arg * arg


def p(num, times):
	thing = num
	for x in range(times - 1):
		thing = thing * num
	return thing

def fac(num):
	thing = num
	if num == 1:
		return
	print num
	print fac(num - 1)


print p(4, 2)
print sq(10)
print p(2, 3)
print fac(5)
