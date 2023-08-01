import datetime

def to_time_object(time_string):
    if len(time_string) > 7:
        prod = (time_string[:2], time_string[3:5], time_string[6:])
    else:
        prod = (time_string[:1], time_string[2:4], time_string[5:])

    if prod[2] == "AM" and prod[0] != "12":
        return datetime.datetime(1, 1, 1, int(prod[0]), int(prod[1]), 1)
    elif prod[2] == "AM" and prod[0] == "12":
        return datetime.datetime(1, 1, 1, int(prod[0])-12, int(prod[1]), 1)
    elif prod[2] == "PM":
        if int(prod[0]) > 11:
            new_hour = int(prod[0])-12
        else:
            new_hour = int(prod[0])
        return datetime.datetime(1, 1, 1, new_hour+12, int(prod[1]), 1)

def add_time(time_string, delta_time):
    time_obj = to_time_object(time_string)

    hour_delta = int(float(delta_time) // 1)
    min_delta = float(delta_time) % 1 * 60

    delta = datetime.timedelta(hours=hour_delta, minutes=min_delta)

    new_time = time_obj + delta
    if new_time.hour >= 12:
        AM_PM = "PM"
        new_time -= datetime.timedelta(hours=12)
    else:
        AM_PM = "AM"

    if new_time.hour == 0:
        new_time += datetime.timedelta(hours=12)

    return (new_time.hour, new_time.minute, AM_PM)


def get_time_makeup(time_string):
    if len(time_string) > 7:
        return (time_string[:2], time_string[3:5], time_string[6:])
    else:
        return (time_string[:1], time_string[2:4], time_string[5:])
