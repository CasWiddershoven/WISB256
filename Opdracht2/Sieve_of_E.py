from math import ceil, sqrt
from sys import argv
from time import perf_counter

def primeSieve(num):
	flags = [True]*(num-2)
	for i in range(2, ceil(sqrt(num))): # For every i (index) in 2 to the square root of the max number given
		if flags[i-2] == True: #If the number isn't marked as non-prime yet
			for j in range(i**2, num, i): #Then every multiple of the number is non-prime, starting (slightly optimized) at that prime squared
				flags[j-2] = False #Mark the number as non-prime
	primes = list()
	for i in range(2, num): #For each number 
		if flags[i-2]:
			primes.append(i)
	return primes

startTime = perf_counter()
maxNum = int(argv[1])
output = argv[2]
outputFile = open(output, 'w')

primes = primeSieve(maxNum)
endTime = perf_counter()
print("Found %s Prime numbers smaller than %s in %s sec." % (str(len(primes)), str(maxNum), str(endTime - startTime)))
print("--------------------------------------------")
outputFile.write("\n".join([str(p) for p in primes]))
