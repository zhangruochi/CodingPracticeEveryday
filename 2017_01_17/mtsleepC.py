#实例化 thread 类

import threading
from time import sleep,ctime
loops = [4,2]

def loop(nloop,nsec):
    print('strat loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop',nloop,'done at: ',ctime())


def main():
    print('starting at: ', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target = loop,args = (i,loops[i]))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print('all DONE at: ', ctime())


if __name__ == '__main__':
    main()        


