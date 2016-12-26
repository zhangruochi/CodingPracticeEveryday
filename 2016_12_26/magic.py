'''
所谓魔法函数（Magic Methods），是Python的一种高级语法，
允许你在类中自定义函数（函数名格式一般为__xx__），并绑定
到类的特殊方法中。比如在类A中自定义__str__()函数，则在
调用str(A())时，会自动调用__str__()函数，并返回相应的
结果。在我们平时的使用中，可能经常使用__init__函数和__del__函数，
其实这也是魔法函数的一种
'''

class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ":" + str(self.age)

    def __lt__(self,other):
        #__lt__函数即less than函数，即当比较两个People实例时自动调用 
        return self.name < other.name if self.name !=  other.name else self.age < other.age


print("\t".join([str(item) for item in sorted([People("abc", 18),\
     People("abe", 19), People("abe", 12), People("abc", 17)])]))


'''
   __call__ 
   Python中有一个有趣的语法，只要定义类型的时候，实现__call__函数，这个类型就成为可调用的。
　 换句话说，我们可以把这个类的对象当作函数来使用，相当于重载了括号运算符。
   也就是说x(arg1, arg2...) 等同于调用x.__call__(self, arg1, arg2)

'''
class DistanceForm(object):
    def __init__(self, origin):
        self.origin = origin
        print("origin :"+str(origin))
    def __call__(self, x):
        print("x :"+str(x))
 
p = DistanceForm(100)
p(2000)
print("")




# eg:  实现一个可以任意深度赋值的字典类，如a[0] = 'value1'; a[1][2] = 'value2'; a[3][4][5] = 'value3'
class MyDict(dict):
    def __setitem__(self,key,value):
        print("setitem:",key,value,self)
        super().__setitem__(key,value)
        return

    def __getitem__(self,item):
        print("getitem:",item,self)
        # 基本思路: a[1][2]赋值时 需要先取出a[1] 然后给a[1]的[2]赋值
        if item not in self:
            temp = MyDict()
            super().__setitem__(item,temp)
            return temp

        return super().__getitem__(item)

test = MyDict() 
test[0] = 'test' 
test[1][2] = 'test1' 
test[3][4][5] = 'test2' 

    
         