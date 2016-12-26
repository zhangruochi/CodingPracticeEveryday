#调用父类中的函数  改函数已经在子类中被覆盖
class A:
    def spam(self):
        print("A.spam")

class B(A):
    def spam(self):
        print("B.spam")

    def print_A_spam(self):
        super().spam()


class Proxy:
    def __init__(self,obj):
        self._obj = obj 

    def __getattr__(self,name):
        return getattr(self._obj,name)

    def __setattr__(self,name,value):
        if name.startswith('_'):
            super().__setattr__(name,value)
        else:
            setattr(self._obj,name,value)


class A(object):  
    def __init__(self):  
        self.name = 'from __dicts__: zdy'  
  
    def __getattr__(self, item):  
        if item == 'name':  
            return 'from __getattr__: zdy'  
        elif item == 'age':  
            return 26  
  
a = A()  
print(a.name) # 从__dict__里获得的  
print(a.age) # 从__getattr__获得的


if __name__ == '__main__':
    b = B()
    b.spam() 
    b.print_A_spam() 
           