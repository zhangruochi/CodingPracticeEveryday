from functools import wraps
import time

def time_func(func):
    @wraps(func)  #为了保存函数的元数据
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__,":",end - start)
        return result
    return wrapper

@time_func
def test(n):
    while n>0:
        n -= 1

test(20000000)            


#解包 对原始数据进行访问  利用 wrapped 属性
test = test.__wrapped__
test(20000000)

