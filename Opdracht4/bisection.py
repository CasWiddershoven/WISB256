from copy import copy

def findRoot(f, a, b, epsilon):
	if (f(a) < 0 and f(b) < 0) or (f(a) > 0 and f(b) > 0):
		raise AssertionError("This function doesn't seem to cross 0!")
	m = (a+b)/2
	if (b-a < epsilon):
		return m
	if (f(m) > 0 and f(b) > 0) or (f(m) < 0 and f(b) < 0):
		return findRoot(f, a, m, epsilon)
	if (f(m) < 0 and f(b) > 0) or (f(m) > 0 and f(b) < 0):
		return findRoot(f, m, b, epsilon)
