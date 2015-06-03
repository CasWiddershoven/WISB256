import numpy
from scipy.integrate import odeint
from scipy.linalg import eigvals

class Lorenz:
	def __init__(self, start, sigma=10, rho=28, beta=8/3):
		self.sigma = sigma
		self.rho = rho
		self.beta = beta
		self.start = start
		
	def func(self, p, t0):
		x = p[0]
		y = p[1]
		z = p[2]
		
		d1 = self.sigma*(y-x)
		d2 = x*(self.rho-z)-y
		d3 = x*y-self.beta*z
		return [d1,d2,d3]
		
	def solve(self, T, dt):
		t = numpy.linspace(0, T, T/dt)
		soln = odeint(self.func, self.start, t)
		return soln
		
	def df(self, u):
		v1 = [-self.sigma, self.rho-u[2], u[1]]
		v2 = [self.sigma, -1, u[0]]
		v3 = [0, -u[0], -self.beta]
		
		return numpy.array([v1, v2, v3])
		
	def isStable(self, u):
		jacobian = self.df(u)
		eigens = eigvals(jacobian)
		if all(val < 0 for val in eigens):
			return True
		return False
