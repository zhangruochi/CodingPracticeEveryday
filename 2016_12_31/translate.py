remap = {
    ord("\t"): ' ',
    ord("\n"): None,
    ord("n"):"m"
}

s = "name\n\tname\n"
print(s.translate(remap))


#删掉所有的 Unicode 字符
import unicodedata
import sys


# sys.maxunicode is "An integer giving the largest supported code point for a Unicode character."
#把字符的权威组合值返回，如果没有定义，默认是返回0
#unicodedata.normalize(form, unistr)  把一串UNICODE字符串转换为普通格式的字符串，具体格式支持NFC、NFKC、NFD和NFKD格式

cmb_chars = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))



c = dict.fromkeys([1,2,3,4],"fuck")
print(c)
#{1: 'fuck', 2: 'fuck', 3: 'fuck', 4: 'fuck'}



#字符串对齐
text = "hello world"
print(text.ljust(20))
print(text.rjust(20))
print(text.ljust(20,"*"))


#> < ^   对齐字符（右对齐  左对齐   居中）
print(format(text,">20"))
print(format(text,"^20"))    


print("{:<20s} {:>20s}".format("Hello","world"))
