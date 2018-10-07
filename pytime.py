from datetime import datetime, date

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


