# see https://www.codewars.com/kata/5a262cfb8f27f217f700000b/solutions/python

def solve(a,b):
    r1 = "".join(x for x in a if x not in b)
    r2 = "".join(x for x in b if x not in a)
    return r1+r2

print(solve("xyab","xzca") == "ybzc")
print(solve("xyabb","xzca") == "ybbzc")
print(solve("abcd","xyz") == "abcdxyz")
print(solve("xxx","xzca") == "zca")