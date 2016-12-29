# 产生的值是有符号的  

x = 1234 
print(bin(x))  #2
print(oct(x))  #8
print(hex(x))  #16

#不出现前缀
print(format(x,"b"))
print(format(x,"o"))
print(format(x,"x"))



#无符号数
x = -1234
print(format(2*32+x,"b"))  #加上最大值


#将不同进制的字符串转化为十进制整数
a = "1111"
print(int(a,2))
print(int(a,16))
print(int(a,8))

