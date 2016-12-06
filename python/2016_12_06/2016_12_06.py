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
        
    


if __name__ == '__main__':
    result = max_rot(99249557)
    print(result)

    