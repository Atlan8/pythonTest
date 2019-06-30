from random import random
from math import sqrt
from time import clock
DARTS = 120000000
hits = 0
clock()
for i in range(1, DARTS):
  x, y = random(), random()
  dist = sqrt(x**2 + y**2)
  if dist <= 1.0:
    hits = hits + 1
pi = 4*(hits/DARTS)
print('pi的值是: %s' %pi)
print('程序的运行时间是: %-5ss' %clock())