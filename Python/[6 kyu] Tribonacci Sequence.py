# More details on this kata
# https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    if n == 0:
        return []
    if n == 1:
        return [signature[0]]
    if n == 2:
        return signature[0:2]
    if n == 3:
        return signature[0:3]
    fib = signature
    for i in range(n):
        fib.append(signature[i] + signature[i + 1] + signature[i + 2])
        if len(fib) == n:
            break
    return fib
