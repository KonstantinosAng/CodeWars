# see https://www.codewars.com/kata/5b358a1e228d316283001892/solutions/python

def get_strings(city):
    letters = {}
    for letter in city:
        if letter.lower() not in letters:
            letters[letter.lower()] = 1
        else:
            letters[letter.lower()] += 1
    return ",".join(key + ":" + "*"*value for key, value in letters.items() if key != " ")


print(get_strings("Chicago") == "c:**,h:*,i:*,a:*,g:*,o:*")
print(get_strings("Bangkok") == "b:*,a:*,n:*,g:*,k:**,o:*")
print(get_strings("Las Vegas") == "l:*,a:**,s:**,v:*,e:*,g:*")