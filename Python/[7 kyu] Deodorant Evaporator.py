# see https://www.codewars.com/kata/5506b230a11c0aeab3000c1f/solutions/python

def evaporator(content, evap_per_day, threshold):
    days = 0
    limit = threshold/100*content
    while content >= limit:
        content -= evap_per_day/100*content
        days += 1
    return days

print(evaporator(10, 10, 10) == 22)