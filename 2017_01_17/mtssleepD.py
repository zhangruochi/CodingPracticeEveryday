#创建 Thread 的实例， 给它一个可以调用的类实例
import threading
from time import sleep, ctime

loops  = [2,4]

class ThreadFunc(object):

    def __init__(self,func,args,name = ''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)



def loop(nloop,nsec):
    print("start loop",nloop,'at:',ctime())
    sleep(nsec)
    print('loop',nloop,'done at:',ctime())

def main():
    print('starting at: ',ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target = ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("all DONE at:",ctime()) 

if __name__ == '__main__':
    main()               



