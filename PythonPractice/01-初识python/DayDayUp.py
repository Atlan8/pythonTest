# DayDayUp.py
# dayfactor = 0.005
dayfactor = 0.01
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)

print('向上: {:0.2f}, 向下: {:0.2f}'.format(dayup, daydown))