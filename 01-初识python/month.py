months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
n = input('请输入月份数（1-12）:')
print(int(n))
if (int(n))<=0 or (int(n))>12:
  print('输入错误')
else:
  pos = (int(n)-1) * 3
  monthAbbrev = months[pos:pos+3]
  print('月份简写是'+monthAbbrev+'.')