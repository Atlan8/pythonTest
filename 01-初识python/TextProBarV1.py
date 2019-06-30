# 一个简易的进度条
import time
import numpy
scale = 10
for i in range(scale + 1):
  a = '*' * i
  b = '.' * (scale - i)
  c = (i/scale) * 100
  print('{:^3.0f}%[{}->{}]'.format(c,a,b))
  time.sleep(0.1)
print('------执行结束------')

# for i in range(101):
#   print('\r{:3}%'.format(i), end="") # print默认会在每行输出的末尾加一个换行符，若使用end则会用end里面的内容代替，\r表示光标回到开头
#   time.sleep(0.1)

scale = 50
print('执行开始'.center(scale//2, '-'))
start = time.perf_counter()
for i in range(scale + 1):
  a = '*' * i
  b = '.' * (scale - i)
  c = (i/scale) * 100
  dur = time.perf_counter() - start
  print('\r{:^3.0f}%[{}{}]{:.2f}s'.format(c,a,b,dur), end='')
  time.sleep(0.1)
print('\n'+'执行结束'.center(scale//2, '-'))