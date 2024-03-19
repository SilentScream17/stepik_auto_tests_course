time_start = '13:52:02.008'
time_end = '14:00:56:196'


def time_convert_millis(time):
    time = time.replace('.', ':')
    times = time.split(":")
    return int(times[0]) * 3600000 + int(times[1]) * 60000 + int(times[2]) * 1000 + int(times[3])


print(time_convert_millis(time_end) - time_convert_millis(time_start))
