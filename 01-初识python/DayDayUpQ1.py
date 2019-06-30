# DayDayUpQ1.py
# 每天进步 1%。
dayup = pow(1.001, 365)
# 每天退步 1%。
daydown = pow(0.999, 365)
print('向上: {: 0.2f}, 向下: {:0.2f}'.format(dayup, daydown))