# see https://www.codewars.com/kata/5635e7cb49adc7b54500001c/solutions/python

def solve(n):
    if str(n)[-1] != "0": return -1
    fifties = n//500
    twenties = (n - fifties*500)//200 if n - fifties*500 >= 0 else 0
    onehundred = (n - fifties*500 - twenties*200)//100 if (n - fifties*500 - twenties*200) >= 0 else 0
    fifty = (n - fifties*500 - twenties*200 - onehundred*100)//50 if (n - fifties*500 - twenties*200 - onehundred*100) >= 0 else 0
    twenty = (n - fifties*500 - twenties*200 - onehundred*100 - fifty*50)//20 if (n - fifties*500 - twenties*200 - onehundred*100 - fifty*50) >= 0 else 0
    ten = (n - fifties*500 - twenties*200 - onehundred*100 - fifty*50 - twenty*20)//10 if (n - fifties*500 - twenties*200 - onehundred*100 - fifty*50 - twenty*20) >= 0 else 0 
    return fifties + twenties + onehundred + fifty + twenty + ten


print(solve(770) == 4)
print(solve(550) == 2)
print(solve(10) == 1)
print(solve(1250) == 4)
print(solve(1500) == 3)  
print(solve(125) == -1)
print(solve(666) == -1)
print(solve(42) == -1)
