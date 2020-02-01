import random


class RandInterface:

    def __init__(self):
        random.seed()

    def getRanEle(self, data: list = []):
        ran = random.randint(0, (len(data)-1))
        return data[ran]

    # def Weighted_NumberGen(self, data_list, weight):
    #     random_int = random.randint(0, 100)
    #     count, low = 0, 0
    #     high = weight[0]
    #     while count < len(weight):
    #         if(low <= random_int <= high):
    #             return data_list[count]
    #         low = low + weight[count]
    #         count = count + 1
    #         high = high + weight[count]

    # def Multi_NumberGen(self, data_list, count):
    #     i = 0
    #     out = []
    #     while i < count:
    #         data = self.Monster_NumberGen(data_list)
    #         j = 0
    #         for item in data_list:
    #             if item == data:
    #                 index = j
    #                 break
    #             j = j + 1
    #         out.append(data)
    #         data_list.pop(index)
    #         i = i + 1
    #     return out
