x = 10
a = lambda y:x+y
x = 20
b = lambda y:x+y



#运行时绑定 而不是在定义的时候绑定
print(a(10))
print(b(10))

'''
30
30
'''


#如果希望匿名函数可以在定义的时候绑定变量 那么可以将那个值作为默认的参数实现



x = 10
a = lambda y,x=x:x+y
x = 20
b = lambda y,x=x:x+y


print(a(10))
print(b(10))

'''
20
30
'''


funcs = [lambda x,n=n : x+n for n in range(5)]
for nunber in funcs:
    print(nunber(0))

'''
0
1
2
3
4
'''    