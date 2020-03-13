# More details on this kata
# https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    unique = arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i] != unique and arr[i+1] != unique: return unique
        if arr[i] != unique and arr[i+1] == unique: return arr[i]
        if arr[i] == unique and arr[i+1] != unique: return arr[i+1]

