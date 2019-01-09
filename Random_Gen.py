import random
    
def Monster_NumberGen(data_list):
    count = 0
    random_int = random.randint(0,100)
    data_listlen = len(data_list)
    data_int = 100/data_listlen
    while count < (data_listlen):
        if (int(count * data_int) <= random_int <= (int(count + 1) *  data_int)):
            return (data_list[count])
        count = count + 1