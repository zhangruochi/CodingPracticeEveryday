_formats = {
    "ymd":'{d.year}-{d.month}-{d.day}',
    "mdy":'{d.month}/{d.day}/{d.year}'
}


class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self,code):
        if code == '':
            code = "ymd"

        fmt = _formats[code]
        return fmt.format(d=self)


d = Date(2016,12,22)
print(format(d))        # 调用 __format__ 函数      

