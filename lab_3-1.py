# Author: Nolan (AMDG) 10/21/2021

import math
import time
t0 = time.perf_counter()

print(math.pow(2, 2))

t1 = time.perf_counter()

speed1 = t1 - t0
print(speed1)

t2 = time.perf_counter()

print(2 ** 2)

t3 = time.perf_counter()

speed2 = t3 - t2
print(speed2)

print(speed2 - speed1)
