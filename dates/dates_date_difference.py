def current_time_in_different_timezones():
    # Get Current Time in different Time Zones
    from datetime import date
    from datetime import timedelta

    # Get Today's Date
    today = date.today()
    print(f'Today is {today}')

    # Get Yesterday's Date
    yesterday = today - timedelta(days=1)
    print(f'Yesterday was {yesterday}')

if __name__=='__main__':
    current_time_in_different_timezones()



