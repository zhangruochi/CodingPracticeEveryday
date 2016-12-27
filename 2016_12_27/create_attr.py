#描述符  就是将某种特殊类型的类的实例指派给另一个类的属性
#只要实现了__get__等三种方法中一个或几个都是描述符类


class Interger:
    def __init__(self,name):
        self.name = name

    def __get__(self,instance,cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self,instance,value):
        if not isinstance(value,int):
            raise TypeError("Expected a int ")

        instance.__dict__[self.name] = value

    def __delete__(self,instance):
        del instance.__dict__[self.name]


class Point:
    x = Interger("x")
    y = Interger("y")

    def __init__(self,x,y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Point(2,3)
    print(p.x) 

    p.x = 2
    p.y = 2.5                                       