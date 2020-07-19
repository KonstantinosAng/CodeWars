# see https://www.codewars.com/kata/5663f5305102699bad000056/solutions/python

def mxdiflg(a1, a2):
    if a2 == [] or a1 == []: return -1
    a1.sort(key=len) ; a2.sort(key=len)
    max1 = abs(len(a1[0]) - len(a2[-1]))
    max2 = abs(len(a1[-1]) - len(a2[0]))
    return max1 if max1 >= max2 else max2



s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(s1, s2) == 13)