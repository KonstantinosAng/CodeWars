# More details on this kata
# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    if seconds == 0: return 'now'
    if seconds == 1: return '1 second'
    if seconds < 60: return '{} seconds'.format(seconds)
    minutes = int(seconds/60)
    secs = seconds - minutes*60
    hours = int(minutes/60)
    minutes = minutes - hours*60
    days = int(hours/24)
    hours = hours - 24*days
    years = int(days/365)
    days = days - years*365
    j, count, add, ret = 0, 0, ['' for x in range(5)], ''
    for s in ([years, days, hours, minutes, secs]):
        if s == 0: continue
        count += 1
    for i, s in enumerate([years, days, hours, minutes, secs]):
        if s == 0: continue
        if count == 1: break
        if count == 2:
            add[i] = ' and '
            break
        if j == count - 2:
            add[i] = ' and '
            break
        add[i] = ', '
        j += 1
    for s, msg, d in zip([years, days, hours, minutes, secs], [' year', ' day', ' hour', ' minute', ' second'], add):
        if s == 0: continue
        elif s == 1: ret += str(s) +  msg
        else: ret += str(s) + msg + 's'
        ret += d
    if ret[-1] == ' ': return ret[:-1]
    return ret

