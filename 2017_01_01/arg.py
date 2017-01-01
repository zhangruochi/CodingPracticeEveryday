


#可接受任意数量的位置参数

def test1(first,*rest):
    print(type(rest)) #<class 'tuple'>
    return (first + sum(rest)) / (len(rest) + 1)


#接受任意数量的关键词参数
import html
'''
   python中，html模块提供了只提供了一个方法：
   html.escape(s, quote = True)
       该方法主要是把html文件中的特殊字符(&,<,>,",'等)转换为HTML-safe字符
'''

def make_element(name,value, **attrs):
    print(type(attrs))  #{'quantity': 6, 'size': 'large'}  <class 'dict'>

    keyvals = [' {}="{}"'.format(item[0],item[1]) for item in attrs.items()]
    attr_str = "".join(keyvals)
    print(attr_str)  #quantity="6" size="large"
    element = '<{name}{attrs}>{value}</{name}>'.format(name = name,attrs = attr_str, value=html.escape(value))

    return element   

# 注意  以*开头的参数只能作为最后一个位置参数   **开头的参数只能作为最后一个参数




#希望函数只能通过关键词的形式传递特定的参数   可以将关键词参数的位置放在以*开头的参数后或者一个单独的*后
def recv(maxsize,*,block):
    pass

          

if __name__ == '__main__':
    print(test1(1,2,3,4,5))
    print(make_element('p','Albatross', size = 'large', quantity=6))
    recv(2014,block=True)
    recv(2014,True)

            





