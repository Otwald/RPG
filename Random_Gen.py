import random
    
def Monster_NumberGen(data_list):
    count = 0
    random_int = random.randint(0,100)
    data_int = 100/(len(data_list))
    while count < len(data_list):
        if (int(count * data_int) <= random_int <= (int(count + 1) *  data_int)):
            return (data_list[count])
        count = count + 1

def Weighted_NumberGen(data_list, weight):
    random_int = random.randint(0,100)
    count, low = 0, 0
    high = weight[0]
    while count < len(weight):
        if(low <= random_int <= high):
            return data_list[count]
        low = low + weight[count]
        count = count + 1
        high = high + weight[count]

def Multi_NumberGen(data_list, count):
    i = 0
    out= []
    while i < count:
        data = Monster_NumberGen(data_list)
        j = 0
        for item in data_list:
            if item == data:
                index = j
                break
            j = j + 1
        out.append(data)
        data_list.pop(index)
        i = i + 1
    return out