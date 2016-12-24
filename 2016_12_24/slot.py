class Test(object):
    pass

class Test2(object):
    __slots__ = ['year','name']
    def __init__(self,name,year):
        self.year = year
        self.name = name



if __name__ == '__main__':
    test = Test()
    test.name = "zhang"
    print(test.__class__)
    print(test.__dict__)
    '''
    <class '__main__.Test'>
    {'name': 'zhang'}
    '''

    test = Test2("zhang","22")
    test.sex = "male"
    print(test.__class__)
    print(test.__dict__)