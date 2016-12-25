# 单下划线总是被认为只属于内部实现

class A:
    def __init__(self):
        pass

    def _internal_method(self):
        pass


#双下划线会出现名称重整
class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print("__private_method")           


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1    # 不会重写 B.__private

    def __private_method(self):
        pass   



# 我们应该让非公开的名称已单下划线开头   除非有些内部属性为了对子类进行隐藏



#创建可管理的属性

class Person(object):
    def __init__(self,first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self.first_name

    @first_name.setter  #必须要先定义 @property
    def first_name(Self,value):
        if not isinstance(value,str):
            raise TypeError("Excepted a string")
        self.first_name = value
    
    @first_name.deleter
    def first_name(self):
        raise AttributeError("can not delete")        
        



#初始化检查
class Person(object):
    def __init__(self,value):
        self.set_first_name(value)

    def get_first_name(self):
        return self.first_name

    def set_first_name(self,value):
        if not isinstance(value,str):
            raise TypeError("Excepted a string")
        self._first_name = value  

    def delete_first_name(self):
        raise AttributeError("can not delete") 



class Test:
    def __init__(self,value):
        self._private_value = value
        self.__private_value = value + "__"

a = Test("zhangruochi") 
print(a._private_value)    #zhangruochi 
print(a._Test__private_value)   #zhangruochi                 



