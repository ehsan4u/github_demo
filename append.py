
l = []
l.append('foo')
l.append('bar')
l.append('baz')

print(l)

s = ''.join(l)

print(s)

var1 = "foo"
var2 = "bar"
var3 = f"{var1}{var2}"
print(var3)    

a='foo'
b='baaz'

a.__add__(b)
print(a)
print(a.__add__(b))