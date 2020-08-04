# see https://www.codewars.com/kata/52cd53948d673a6e66000576/solutions/python

from TestFunction import Test

def search(titles, term): 
    return list(filter(lambda title: term in title.lower(), titles))

test = Test(None)
titles = ['The Big Bang Theory', 'How I Met Your Mother', 'Dexter', 'Breaking Bad', 'Doctor Who', 'The Hobbit', 'Pacific Rim', 'Pulp Fiction', 'The Avengers', 'Shining']
test.assert_equals(search(titles, 'ho'), ['How I Met Your Mother', 'Doctor Who', 'The Hobbit'])
test.assert_equals(search(titles, 'exte'), ['Dexter'])
test.assert_equals(search(titles, 'the'), ['The Big Bang Theory', 'How I Met Your Mother', 'The Hobbit', 'The Avengers'])	
