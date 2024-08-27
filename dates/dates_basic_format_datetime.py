def dates_format_datetime():
    # The date contains year, month, day, hour, minute, second, and microsecond.
    # We can format date time as per our requirements

    # Import Date Time Module
    import datetime as dt

    # Print Year, Month, and Day on separate lines
    x = dt.datetime.now()
    print(x.year) # 2023
    print(x.month) # 9
    print(x.day) # 29

    # Print Hour, Minutes and Seconds
    print(x.hour) # 20
    print(x.minute) # 45
    print(x.second) # 48

    # Print Weekday Short and Long Version
    print(x.strftime('%a')) # Fri
    print(x.strftime('%A')) # Friday

    # Print Month Name Short and Long Version
    print(x.strftime('%b')) #Sep
    print(x.strftime('%B')) #September

    # Print Year Short and Long Version
    print(x.strftime('%y')) #23
    print(x.strftime('%Y')) #2023

    # %w - Weekday as a number 0-6, 0 is Sunday
    print(x.strftime('%w'))
    # %d-	Day of month 01-31
    print(x.strftime('%d'))

    # %m	Month as a number 01-12
    print(x.strftime('%m'))
    # %y	Year, short version, without century 18
    print(x.strftime('%y'))
    # %Y	Year, full version	2018
    print(x.strftime('%Y'))

    # %H	Hour 00-23	17
    print(x.strftime('%H'))
    # %I	Hour 00-12	05
    print(x.strftime('%I'))
    # %p	AM/PM	PM
    print(x.strftime('%p'))

    # %M	Minute 00-59	41
    print(x.strftime('%M'))
    # %S	Second 00-59	08
    print(x.strftime('%S'))
    # %f	Microsecond 000000-999999	548513
    print(x.strftime('%f'))

    # %z	UTC offset	+0100
    print(x.strftime('%z'))
    # %Z	Timezone	CST
    print(x.strftime('%Z'))
    # %j	Day number of year 001-366	365
    print(x.strftime('%j'))
    # %U	Week number of year, Sunday as the first day of week, 00-53	52
    print(x.strftime('%U'))
    # %W	Week number of year, Monday as the first day of week, 00-53	52
    print(x.strftime('%W'))


    # %c	Local version of date and time	Mon Dec 31 17:41:00 2018
    print(x.strftime('%c'))
    # %C	Century	20
    print(x.strftime('%C'))
    # %x	Local version of date	12/31/18
    print(x.strftime('%x'))
    # %X	Local version of time	17:41:00
    print(x.strftime('%X'))

    # %G	ISO 8601 year	2018
    print(x.strftime('%G'))
    # %u	ISO 8601 weekday (1-7)	1
    print(x.strftime('%u'))
    # %V	ISO 8601 weeknumber (01-53)	01
    print(x.strftime('%V'))

if __name__=='__main__':
    dates_format_datetime()
    