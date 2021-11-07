from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

simdi  = datetime.now() 
simdi  = datetime.today()

result = simdi.now().year
result = simdi.now().month
result = simdi.now().day
result = simdi.now().hour
result = simdi.now().minute
result = simdi.now().second

result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%d')
result = datetime.strftime(simdi,'%A')
result = datetime.strftime(simdi,'%B')
result = datetime.strftime(simdi,'%Y %B %A')

t = '15 April 2021 hour 10:12:30'

result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
result = result.year

birthday = datetime(1991,9,15,1,13,12)


result = datetime.timestamp(birthday) #saniye
result = datetime.fromtimestamp(result)#saniye to datetime
result = datetime.fromtimestamp(0)


result = simdi - birthday   # timedelta

# result = result.days
# result = result.microseconds
print(simdi)
# result = simdi + timedelta(days=10)
result = simdi + timedelta(days=730,minutes= 10)

result = simdi - timedelta(days = 10)
print(result)

