#strip lstrip rstrip    默认去掉空格符(" ", "\n")  也可以传递参数

a = " ---Hello world=====\n"

print(a.strip())
print(a)


b = "---Hello world====="
c = "Hello world====="

print(b.strip("-="))
print(c.strip("-="))



#如果需要对字符串中间的字符进行操作   可以用 replace 和 re
s = "hello world   \n"
print(len(s))
print(len(s.strip("\n")))
print(s.strip().replace(" ",","))
print(s)




#读取文件 创建迭代器
with open("test.txt","r") as f:
    lines = (line.strip() for line in f)

for lines in lines:
    pass     

