# see https://www.codewars.com/kata/55955a48a4e9c1a77500005a/solutions/python

def greet(name):
    return "hello " + name + "!" if name is not None and name != "" else None

print(greet("Niks") == "hello Niks!")
print(greet("Nick") == "hello Nick!")
print(greet("") == None)
print(greet(None) == None)