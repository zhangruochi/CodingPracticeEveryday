def test():
    sequence = 0
    def change():
        #sequence = sequence + 1   报错
        sequence = 1
        print("in: {}".format(sequence))
    change()    
    print("out: {}".format(sequence))


def test2():
    sequence = 0
    def change():
        nonlocal sequence
        sequence = 2
        print("in: {}".format(sequence))
    change()    
    print("out: {}".format(sequence))    


if __name__ == '__main__':
    test()   
    print('-------------')
    test2()

