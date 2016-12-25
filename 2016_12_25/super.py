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



if __name__ == '__main__':
    b = B()
    b.spam() 
    b.print_A_spam() 

    p = Proxy("zhangruochi")  
    print(p)                