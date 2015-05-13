from math import log
from sys import argv

primes = [int(p) for p in open(argv[1]).readlines()]
print("{:<14}=  {}".format("Largest Prime", primes[-1]))
print("--------------------------------  ")
print("{:<14}=  {}".format("pi(N)", len(primes)))
print("{:<14}=  {}".format("N/log(N)", primes[-1]/log(primes[-1])))
print("{:<14}=  {}".format("ratio", len(primes)*log(primes[-1])/primes[-1]))
print("--------------------------------  ")
print("{:<14}=  {}".format("pi_2(N)", len([primes[p] for p in range(len(primes)) if p + 1 < len(primes) and primes[p] + 2 == primes[p+1]])))
print("{:<14}=  {}".format("2CN/log(N)^2", 2*0.6601618*primes[-1]/(log(primes[-1])**2)))
print("{:<14}=  {}".format("ratio", len([primes[p] for p in range(len(primes)) if p + 1 < len(primes) and primes[p] + 2 == primes[p+1]])/(2*0.6601618*primes[-1]/(log(primes[-1])**2))))