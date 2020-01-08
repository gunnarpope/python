"""A variety of ways to represent real-time timesamps"""


import datetime
import time

timestamp = datetime.date.fromtimestamp(time.time()).isoformat()
print(timestamp)
# 2020-01-08

timestamp = time.strftime("%m-%d-%Y %H:%M:%S")
print(timestamp)
# '01-08-2020 13:50:12'

timestamp = time.strftime("%H:%M:%S")
print(timestamp)
# '13:51:11'

