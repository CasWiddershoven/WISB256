from array import array

class Vector:
	def __init__(self, n, filler=0):
		if isinstance(filler, list) or isinstance(filler, array):
			self.data = array('d', filler)
		else:
			self.data = array('d', [filler]*n)

	def __str__(self):
		return "\n".join(["{:.6f}".format(d) for d in self.data])

	def lincomb(self, other, alpha, beta):
		return Vector(len(self.data), [alpha*self.data[i]+beta*other.data[i] for i in range(len(self.data))])
		
	def scalar(self, alpha):
		return self.lincomb(Vector(len(self.data)), alpha, 0)
		
	def inner(self, other):
		return sum([self.data[i]*other.data[i] for i in range(len(self.data))])
		
	def norm(self):
		return self.inner(self)**0.5

def GrammSchmidt(V):
	def proj(u, v):
		return u.scalar(u.inner(v)/u.inner(u))
	
	for i in range(len(V)):
		V[i] = V[i].scalar(1/V[i].norm())
		for j in range(i+1, len(V)):
			V[j] = V[j].lincomb(proj(V[i], V[j]), 1, -1)
	return V
