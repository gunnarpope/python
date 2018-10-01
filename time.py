from datetime import datetime, date

def getNowTime():
    return ( time.__format__("%Y-%m-%dT%H-%M-%S") )


if __name__ == '__main__':
    time = datetime.now()
    date = date.today()

    nowtime = getNowTime()
    print( nowtime )
    print(date)
    print(time.year)
    print(time.day)
    print(time.month)
    print(time.hour)
    print(time.minute)
    print(time.second)
    print(time.microsecond)

    iso = date.isocalendar()
    print("ISO year: ", iso[0])
    print("ISO weeknumber: ", iso[1])
    print("ISO day: ", iso[2], "(1 = Monday)")




