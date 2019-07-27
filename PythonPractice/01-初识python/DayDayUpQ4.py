# DayDayUpQ4.py
def dayUp(df):
  dayup = 1
  for i in range(365):
    if i % 7 in [6,0]:
      dayup = dayup * (1 - 0.01)
    else:
      dayup = dayup * (1 + df)
  return dayup
dayfactor = 0.01
while dayUp(dayfactor) < 37.78:
  dayfactor += 0.001

print('工作日的努力参数是: {: 0.3f}'.format(dayfactor))

# 星座符号 Unicode 码
for i in range(12):
  print('\n' + chr(9800 + i))
print(chr(10004))
# 字符串填充操作
print('python'.center(20, '='))