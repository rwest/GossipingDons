

def circle(n):
	"""The simple call-the-guy-on-your-right-twice algorithm"""
	return 2*n-1

def divide(n):
	"""My clever algorithm where you divide into two groups who then call each other"""
	if n==1: return 0
	if n==2: return 1
	if n==3: return 3
	smallgroup = int(n/2.0)
	biggroup = int(n/2.0 + 0.5)
	return divide(smallgroup) + divide(biggroup) + smallgroup


print "n	circle	divide"
for i in range(2,100):
	n=i
	print '%d\t%d\t%d'%(n, circle(n), divide(n))

