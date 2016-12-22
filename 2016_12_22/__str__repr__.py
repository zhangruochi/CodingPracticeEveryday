"""
str()函数得到的字符串可读性好（故被print调用），
而repr()函数得到的字符串通常可以用来重新获得该对象，
通常情况下 obj==eval(repr(obj)) 这个等式是成立的。
这两个函数接受一个对象作为其参数，返回适当的字符串
"""

class Test(object):
    def __init__(self,x):
        self.x = x

    def add(self,y):
        return self.x + y

    def __str__(self):
        return "test __str__"   

    def __repr__(self):
        return "test __repr__"     


x = Test(1)
print(x.add(2))  
print(x)   #  调用 __str__
print("object is {0}".format(x))
print("object is {0!r}".format(x))  #!r 调用 __repr__方法



          