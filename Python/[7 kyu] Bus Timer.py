# see https://www.codewars.com/kata/5736378e3f3dfd5a820000cb/solutions/python

def bus_timer(current_time):
    hours, min = current_time.split(":")
    hours, min = int(hours), int(min)
    #print(current_time)
    if hours < 6:
        if hours == 5 and min > 55: return 70 - min
        return 355 - min - 60*hours
    else:
        if hours == 23 and min > 55: return 415 - min
        if min <= 10: return 10 - min
        elif min <= 25: return 25 - min
        elif min <= 40: return 40 - min
        elif min <= 55: return 55 - min
        else: return 70 - min

print(bus_timer("10:00") == 10)
print(bus_timer("15:05") == 5)
print(bus_timer("06:10") == 0)