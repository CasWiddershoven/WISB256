from math import log, floor
from sys import argv
from time import perf_counter

startTime = perf_counter()

realMaxNum = int(argv[1])
maxNum = int((realMaxNum - (realMaxNum % 2) - 2)/2)
output = argv[2]
outputFile = open(output, 'w')

ints = list(range(1, maxNum+1))
j = 1
while 3*j < maxNum:
	i = 1
	while i <= j and i + j + 2*i*j <= maxNum:
		ints[i+j+2*i*j-2] = 0
		i += 1
	j += 1

primes = [2]
for i in ints:
	if i != 0:
		primes.append(2*i+1)

endTime = perf_counter()
print("Found %s Prime numbers smaller than %s in %s sec." % (str(len(primes)), str(realMaxNum), str(endTime - startTime)))
print("--------------------------------------------")
outputFile.write("\n".join([str(p) for p in primes]))
