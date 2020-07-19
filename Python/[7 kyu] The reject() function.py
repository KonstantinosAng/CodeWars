# see https://www.codewars.com/kata/52988f3f7edba9839c00037d/solutions/python

def reject(seq, predicate): 
    return [x for x in seq if not predicate(x)]

print(reject([1, 2, 3, 4, 5, 6], lambda x: x%2==0) == [1, 3, 5])
print(reject(['a', 'b', 3, 'd'], lambda x: type(x)==int) == ['a', 'b', 'd']);
print(reject(['a', 'b', 3, 'd'], lambda x: type(x)==str) == [3]);