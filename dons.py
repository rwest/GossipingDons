

def f(n):
	"""The simple call-the-guy-on-your-right-twice algorithm"""
	return 2*n-1

def g(n):
	"""My clever algorithm where you divide into two groups who then call each other"""
	if n==2: return 1
	return 2*f(n/2) + n/2


for i in range(1,10):
	a=2**i
	print 'n=%d, f(n)=%d, g(n)=%d'%(a, f(a), g(a))

