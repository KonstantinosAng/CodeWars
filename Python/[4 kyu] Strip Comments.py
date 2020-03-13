# More details on this kata
# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def solution(string,markers):
    if len(string) == 0:
        return ''
    t, tt, test, l, j, ret= [], [], [], [], [], ''
    s = string.split('\n')
    for _s in s:
        for m in markers:
            if _s.find(m) != -1:
                t.append(_s.find(m))
        test.append(t)
        t = []
    for a in test:
        tt.append(sorted(a))
    for i, _s in zip(tt, s):
        if i == []:
            l.append(_s)
        if i != []:
            l.append(_s[:i[0]])
    for s in l:
        if s != '':
            if s[-1] == ' ':
                j.append(s[:-1])
                continue
            else:
                j.append(s)
                continue
        else:
            j.append(s)
    for i, s in enumerate(j):
        if i == len(j) - 1:
            ret += s
            continue
        ret += s + '\n'
    return ret
