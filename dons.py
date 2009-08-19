# Each of n elderly dons knows a piece of gossip not known to any of the
# others. They communicate by telephone, and in each call the two dons
# concerned reveal to each other all the information they know so far. What is
# the smallest number of calls that can be made in such a way that, at the
# end, all the dons know all the gossip?

def small(n):
	"""Some special cases for small n"""
	smalldict = {1:0, 2:1, 3:3, 4:4}
	return smalldict[n]
	
def circle(n):
	"""The simple call-the-guy-on-your-right-twice algorithm"""
	return 2*n-1

def divide(n):
	"""My 'clever' algorithm where you divide into two groups who then call each other"""
	if n<=3: return small(n)
	smallgroup = int(n/2.0)
	biggroup = int(n/2.0 + 0.5)
	return divide(smallgroup) + divide(biggroup) + smallgroup

def foursquare(n):
	"""Do it smart with a group of four, else just call the guy ahead. 
	
	Tijdeman, R. "On a Telephone Problem." Nieuw Archief voor Wiskunde 19, 188-192, 1971.
	http://mathworld.wolfram.com/Gossiping.html
	"""
	if n<=3: return small(n)
	if n==4: return 4
	return 2 + foursquare(n-1)


functions = [circle, divide, foursquare]
# print column headings
print "n\t",
for function in functions:
	print '%s\t'%function.__name__,
print
# print table of results
for n in range(2,50):
	print '%d\t'%n,
	for function in functions:
		print '%d\t'%function(n),
	print
print "psyche rocks"

