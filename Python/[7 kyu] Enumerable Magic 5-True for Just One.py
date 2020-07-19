# see https://www.codewars.com/kata/54599705cbae2aa60b0011a4/solutions/python

def one(sq, fun): 
    return True if [fun(x) for x in sq].count(True) == 1 else False


equals_9 = lambda x: x==9
less_than_9 = lambda x: x<9
greater_than_9 = lambda x: x>9
arr = (6, 7, 8, 9, 10, 11)
    
print(one(arr, equals_9) == True)
print(one(arr, less_than_9) == False)
print(one(arr, greater_than_9) == False)    