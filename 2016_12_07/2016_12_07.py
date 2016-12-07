import re
def autocorrect(input):
    pattern = re.compile(r'(?i)\b(u|you+)\b')
    return re.sub(pattern,"your sister", input)

# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

import math
def triangle_type(a, b, c):
    angle_max = max(a**2 + b**2)    

def longest(s1, s2):
    return sorted("".join(set(list(s1 + s2))))



def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise

    if int(sq**0.5) ** 2 != sq:
        return -1
    else:
        return int((sq**0.5 + 1)**2)


def order(sentence):
    word_list = sentence.split(" ")
    number_list = []
    for chr in sentence:
        if chr.isdigit():
            number_list.append(int(chr))
    result_dict = {}        
    for word,number in zip(word_list,number_list):
        result_dict[word] = number

    sorted_list = sorted(result_dict.items(),key = lambda x:x[1])  
    return " ".join([item[0] for item in sorted_list]) 


def order_2(words):
    for word in words.split():
        print(sorted(word))
    return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
            

  



def test():
    if 12.0 == 12:
        print(True)


if __name__ == '__main__':
    order_2("is2 Thi1s T4est 3a")
              