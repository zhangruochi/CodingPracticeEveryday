def dashatize(num):
    if num ==  None:
        return "None"
    if num == 0:
        return "0"
    num = abs(num)    
    result = ""
    num_len = len(str(num))
    num_index = 0
    for num in str(num):
        if int(num) % 2 != 0:
            if num_index == 0:
                result += "{}-".format(num)
            elif num_index == num_len-1:
                result += "-{}".format(num)
            else:
                result += "-{}-".format(num)
        else:
            result += num 
        num_index += 1    
        result = result.replace("--","-") 
    return result  



if __name__ == '__main__':
    string = dashatize(34567)
    print(string)
   