# print('hello world')
# print('yooo')
# 利用IPO的方法来编写程序
# 摄氏度与华氏度的转换
val = input('请输入带温度标识符的温度值（例如：32C）：')
if val[-1] in ['C','c']:
  f = 1.8 * float(val[0:-1]) + 32
  print('转换后的温度为：%0.2fF'%f)
elif val[-1] in ['F','f']:
  c = (float(val[0:-1]) - 32) / 1.8
  print('转换后的温度为：%0.2fC'%c)
else:
  print('输入有误')