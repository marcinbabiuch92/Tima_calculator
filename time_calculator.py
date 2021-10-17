def add_time(start, duration, weekday=''):
    # week's days
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # data preparation
    base = start.split()
    time_b = base[0].split(':')
    time_m = duration.split(':')
    day = str()
    day_part = base[1]

    hour = str((int(time_b[0]) + int(time_m[0])) % 12)
    if hour == '0':
        hour = '12'
    minutes = str((int(time_b[1]) + int(time_m[1])) % 60)
    cycle = (int(time_m[0]) - (int(time_m[0]) % 12)) / 12
    day_counter = 0

    rest = int(time_m[0]) % 12

    # if minutes makes another hour
    if int(time_b[1]) + int(time_m[1]) >= 60:
        hour = str(int(hour) + 1)
        if hour == '12':
            if day_part == 'AM':
                day_part = 'PM'
            else:
                day_counter += 1
                day_part = 'AM'
                day = " (next day)"

    # determining what part of day it is
    if (int(time_b[0]) + rest) >= 12:
        if day_part == 'AM':
            day_part = 'PM'
        else:
            day_counter += 1
            day_part = 'AM'
            day = " (next day)"

    for time in range(0, int(cycle)):
        if day_part == 'AM':
            day_part = 'PM'
        else:
            day_counter += 1
            day_part = 'AM'
            day = ' (next day)'

    if base[1] == 'PM' and day_counter > 1:
        day = ' (' + str(int(day_counter)) + ' days later)'
    elif base[1] == 'AM' and day_counter > 1:
        day = ' (' + str(int(day_counter)) + ' days later)'

    # this loop move through days thanks to day_counter
    index = day_counter % 7
    for dayname in week:
        if weekday == '':
            break
        if weekday.lower() == dayname.lower():
            weekday = ', ' + str(week[(week.index(dayname) + int(index)) % 7])

    return hour + ':' + minutes.zfill(2) + ' ' + day_part + weekday + day
