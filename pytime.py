"""pytime
   A series of time convertion scripts that are helpful.
"""

#-------------------------------------------------
# Copyright © Gunnar Pope 2019
# Liscense: MIT
#-------------------------------------------------

from datetime import datetime, date
import time


def getDateTimeStamp(datestamp, timestamp):
    """Use this function after the upload to convert timestamps to iso format
       Input
           - datestamp = 05252017 for May 25th, 2017
           - timestamp: a string of the format '04082017' for 'DOW:HH:MM:SS'
       Output
           - a datetime object representing the date to the 0.5 second resolution
    """
       #parse the time stamp, from R->L to work around leading zero troubles
    dow = int(timestamp[:-6])
    hr = int(timestamp[-6:-4])
    mm = int(timestamp[-4:-2])
    ss = int(timestamp[-2:])

    t = time(hr, mm,ss) #24Hour, Min, Sec, Microsecond

    YYYY = datestamp[4:]
    MM = datestamp[:2]
    DD = datestamp[2:4]
    date = YYYY + '-' + MM + '-' + DD
    date

    #grab the day of the week when the data was downloadedM
#     dt_day = datetime.strptime(date, '%Y-%m-%d')
    dt_day = DOWtoDatetime(date,dow)

    dt = datetime.combine(dt_day, t)
    return (dt)


def getNowTime():
    time = datetime.now()
    return ( time.__format__("%Y-%m-%dT%H-%M-%S") )

def getNowTimeMicroSec():
    time = datetime.now()
    return ( time.__format__("%Y-%m-%dT%H-%M-%S.%f") )

def getDOW():
    """Returns Day of the Week where Sunday=0"""
    d = date.today()
    iso = d.isocalendar()
    DOW = iso[2]

    if (DOW == 7):
        DOW = 0

    return DOW

def getYear():
    time = datetime.now()
    return time.year

def getMonth():
    time = datetime.now()
    return time.month

def getDay():
    time = datetime.now()
    return time.day

def getHour():
    time = datetime.now()
    return time.hour

def getMinute():
    time = datetime.now()
    return time.minute

def getSecond():
    time = datetime.now()
    return time.second

def getMicrosecond():
    time = datetime.now()
    return time.microsecond





if __name__ == '__main__':

    print( getYear())
    print( getMonth())
    print( getDay())
    print( getDOW())
    print( getHour())
    print( getMinute())
    print( getSecond())
    print( getNowTimeMicroSec())
    print( getNowTime())
