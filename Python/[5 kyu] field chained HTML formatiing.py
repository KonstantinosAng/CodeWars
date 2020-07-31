# see https://www.codewars.com/kata/5e98a87ce8255200011ea60f/solutions

from TestFunction import Test

class Format:
    
    def __init__(self, tag = '{}'):
        self.tag = tag
        
    def __call__(self, *args):
        return self.tag.format(''.join(args))
    
    def __getattr__(self, name):
        return Format(self.tag.format(f'<{name}>{"{}"}</{name}>'))
        
format = Format()
  

format = Format()
test = Test(None)
test.assert_equals(format.div("Foo"), "<div>Foo</div>")
test.assert_equals(format.div.h1("Foo"), "<div><h1>Foo</h1></div>")
test.assert_equals(format.div("Foo", "Bar"), "<div>FooBar</div>")
wrap_in_div = format.div
test.assert_equals(wrap_in_div("Foo"), "<div>Foo</div>")
