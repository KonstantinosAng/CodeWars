# More details on this kata
# https://www.codewars.com/kata/52b7ed099cdc285c300001cd

def sum_of_intervals(intervals):
    s, ret = [list(x) for x in sorted(intervals)], 0
    if len(s) == 1: return abs(s[0][0] - s[0][1])
    for i in range(len(s)):
        if i + 1 > len(s) - 1: break
        if s[i][0] <= s[i + 1][0] <= s[i][1]:
            if i + 1 > len(s) - 1: break
            while s[i][0] <= s[i + 1][0] <= s[i][1]:
                if s[i][1] <= s[i + 1][1]:
                    s[i][1] = s[i + 1][1]
                del s[i + 1]
                if i + 1 > len(s) - 1: break
    for i in s:
        ret += abs(i[0] - i[1])
    return ret

