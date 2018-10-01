from datetime import datetime, date

if __name__ == '__main__':
    time = datetime.now()
    date = date.today()

    print(time)
    print(date)
    print(time.year)
    print(time.day)
    print(time.month)
    print(time.hour)
    print(time.minute)
    print(time.second)
    print(time.microsecond)


