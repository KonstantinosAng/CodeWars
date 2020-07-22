# see https://www.codewars.com/kata/535474308bb336c9980006f2/solutions/python

def greet(name): 
    return f"Hello {name.lower().capitalize()}!"


print(greet('riley') == 'Hello Riley!')
print(greet('molly') == "Hello Molly!")
print(greet('BILLY') == "Hello Billy!")
