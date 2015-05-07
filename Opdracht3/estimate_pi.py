#!/usr/bin/env python3

from random import random, seed, vonmisesvariate as random0toPi
from math import sin, asin, floor, sqrt
from sys import argv

def drop_needle(L):
	# This function drops a needle of length L uniformly in [0,1]xR and checks if it crosses a line  x = 0 or x = 1
	# (We aren't interested in the y coordinate, so we won't calculate it)
	x = random() # Take x random in [0,1]
	T = random0toPi(0, 0) # Take the angle the needle makes with the line x = c random in [0, 2pi]
	if floor(x) != floor(x + L * sin(T)): # If the needle crosses the line x = c, c in N
		return True
	return False
	
def calc_pi(L, N, counter):
	# This function calculates pi based on the frequency the needle crosses the integer lines and the length of the needle
	if L <= 1:
		return 2 * L * N / counter
	LHS = counter / N # LHS is the Left Hand Side of the equation P = 2*L/pi - 2/pi*(sqrt(L^2-1)+arcsin(L^-1)) + 1
	LHS -= 1 # P - 1 = 2*L/pi - 2/pi*(sqrt(L^2-1)+arcsin(L^-1)) = 1/pi*(2*L - 2*(sqrt(L^2-1)+arcsin(L^-1)))
	LHS /= 2*L - 2*(sqrt(L*L - 1) + asin(1/L)) # (P - 1) / (2*L - 2*(sqrt(L^2-1)+arcsin(L^-1))) = 1/pi
	return 1/LHS # 1/((P - 1) / (2*L - 2*(sqrt(L^2-1)+arcsin(L^-1)))) = pi

if __name__ == "__main__":
	if len(argv) < 3 or len(argv) > 4:
		print("Use: estimate_pi.py N L [S]")
		exit(1) # Exit with an error code
	if float(argv[2]) < 0:
		raise AssertionError("L can't be negative")
	if len(argv) == 4:
		seed(int(argv[3])) # Set the given seed
	N = int(argv[1])
	L = float(argv[2])
	counter = 0
	for i in range(N): # Drop the needle N times
		if drop_needle(L):
			counter += 1 # And count the crosses
	print("%d hits in %d times" % (counter, N))
	pi = calc_pi(L, N, counter)
	print("Pi = %f" % pi)
