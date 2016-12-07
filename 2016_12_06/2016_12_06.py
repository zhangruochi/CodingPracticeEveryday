from collections import Counter
def is_isogram(string):
    string_dict = Counter(string.upper())
    print(string_dict)
    if len(string_dict.values()) == sum(string_dict.values()):
        return True
    else:
        return False


count=0;
def calculate_years(principal, interest, tax, desired):
    global count
    if principal >= desired:
        return  count
    else:
        count += 1
        return calculate_years(principal+ principal*interest*(1 - tax), interest, tax, desired)        

def max_rot(n):
    n = str(n)
    result = [n]
    for i in range(len(n)-1):
        n = n[0:i] + n[i+1:] + n[i]
        print(n)
        result.append(int(n))    
    return max(result)

def anagrams(word, words):
    result = []
    for item in words:
        if set(list(item)) == set(list(word)):
            result.append(item)

    return result        

def sum_pairs(ints, s):
    result_dict = {}
    for index_i,value_i in enumerate(ints):
        for index_j,value_j in enumerate(ints):
            if index_i == index_j:
                continue
            if value_i + value_j == s:
                result_dict[(value_i,value_j)] = index_i + index_j

    print(sorted(result_dict.items(),key = lambda x:x[1]))          


    


if __name__ == '__main__':
    print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
    