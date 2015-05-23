import bisection
from math import cos

print(bisection.findAllRoots(lambda x: cos(x), 0, 10, 0.1))
