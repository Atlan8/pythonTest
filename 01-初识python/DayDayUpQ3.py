# DayDayUpQ3.py
# 工作日进步1%，双休退步1%
dayup = 1.0
dayfactor = 0.01
for i in range(365):
  if i % 7 in [6,0]:
    dayup = dayup * (1-dayfactor)
  else:
    dayup = dayup * (1+dayfactor)

print('成长曲线: {: 0.2f}'.format(dayup))