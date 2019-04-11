"""pytime
   A series of time convertion scripts that are helpful.
"""

#-------------------------------------------------
# Copyright © Gunnar Pope 2019
# Liscense: MIT
#-------------------------------------------------

from datetime import *
import numpy as np
import time

def getRealTimeArray(starttime, stepsize,length):
    """
    INPUT:
        stattime = a python datetime object (ie, datetime.now() )
        stepsize = in seconds (ie, stepsize= 0.5sec)
        length   = the desired length of output array
    OUTPUT:
        mytime = datetime(2019,2,20)
        timearray = getRealTimeArray(mytime, 500000,5)
        print('Print out time array')
        for t in timearray:
            t = t.__format__("%Y-%m-%dT%H-%M-%S.%f")
            print(t)
        2019-02-20T00-00-00.000000
        2019-02-20T00-00-00.500000
        2019-02-20T00-00-01.000000
        2019-02-20T00-00-01.500000
        2019-02-20T00-00-02.000000
    """
    rt_array = [starttime + timedelta(0,0,N*stepsize*1e6) for N in range(length) ]
    return rt_array

def plotRealTimeVsData(datetime_array,data):
    """Input: a datetime object in format '2017-03-29T12:55:59.500000'"""
    plt.xticks( rotation=25 )
    ax=plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S%f')
    ax.xaxis.set_major_formatter(xfmt)

    plt.plot(datetime_array,data)
    plt.show()


def getDateTimeStamp(datestamp, timestamp):
    """Use this function after the upload to convert timestamps to iso format
       Input
           - datestamp = '05252017' for May 25th, 2017
           - timestamp = '04081013' for 'DOW:HH:MM:SS'
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

def getDayOfYear():
 		return datetime.now().timetuple().tm_yday



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
    mytime = datetime(2019,2,20)
    timearray = getRealTimeArray(mytime, 0.5,5)
    print('Print out time array')
    for t in timearray:
        t = t.__format__("%Y-%m-%dT%H-%M-%S.%f")
        print(t)
