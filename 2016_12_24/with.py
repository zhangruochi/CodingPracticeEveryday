#遇到 with 语句时  __enter__() 首先被触发执行   返回值放回 as 变量中   最后 __exit__()执行清理工作


from socket import socket, AF_INET,SOCK_STREAM

class LazyConnection(object):
    def __init__(self,address,family = AF_INET,sock_type =  SOCK_STREAM):
        self.address = address
        self.family = family   #域
        self.type = sock_type  # 类型
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError("Already connect.....")

        self.sock = socket(self.family,self.type)
        self.sock.connect(self.address)
        return self.sock


    def __exit__(self,exc_ty,exc_val,tb):
        self.sock.close()
        self.sock = None


#实现多个 with 以嵌套的方式使用 sock 连接

class LazyConnection2(object):
    def __init__(self,address,family = AF_INET,sock_type =  SOCK_STREAM):
        self.address = address
        self.family = family   #域
        self.type = sock_type  # 类型
        self.connections = []

    def __enter__(self):
        sock = socket(self.family,self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock


    def __exit__(self,exc_ty,exc_val,tb):
        self.connections.pop().close()      

    
if __name__ == '__main__':
    from functools import partial
    conn = LazyConnection(("www.python.org",80))
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv,8192),b''))
        print(resp)


 