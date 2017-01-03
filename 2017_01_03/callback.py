#回调函数

def apply_async(func,args,*,callback):
    '''
    a = (1,2)
    print(*a)  
    解包
    '''
    result = func(*args)
    callback(result)

def print_result(result):
    print("Got: ",result)


def add(x,y):
    return x+y



#希望回调函数可以携带额外的状态以便在回调函数中使用
#使用绑定方法

class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self,result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))

#也可以利用闭包来绑定
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence 
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result)) 
    return handler                       



if __name__ == '__main__':
    apply_async(add,(2,3),callback = print_result)

    r = ResultHandler()
    apply_async(add,(2,3),callback = r.handler)  

    handler = make_handler()
    apply_async(add,(2,3),callback = handler) 
          
