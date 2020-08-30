# see https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/solutions/python


def clean_string(s):
    rv = ''
    for letter in s:
        if letter != '#':
            rv += letter
        else:
            rv = rv[:-1]
    return rv


from TestFunction import Test
Test = Test(None)
Test.assert_equals(clean_string('abc#d##c'), "ac")
Test.assert_equals(clean_string('abc####d##c#'), "" )
Test.assert_equals(clean_string("#######"), "" )
Test.assert_equals(clean_string(""), "" )
