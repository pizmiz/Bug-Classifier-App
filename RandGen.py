from random import randint

def GenerateNums():
    NumList = []
    for _ in range(10):
        value = randint(0,10)
        NumList.append(value)

    return NumList


def GenerateNames():
    NumList = GenerateNums()
    NameList = []
    for num in NumList:
        if num == 0:
            NameList.append("Billy")
        elif num == 1:
            NameList.append("Jimmy")
        elif num == 2:
            NameList.append("Jeff")
        elif num == 3:
            NameList.append("Simba")
        elif num == 4:
            NameList.append("Jeramiah")
        elif num == 5:
            NameList.append("Crawford")
        elif num == 6:
            NameList.append("Clements")
        elif num == 7:
            NameList.append("Cletus")
        elif num == 8:
            NameList.append("Cremshaw")
        elif num == 9:
            NameList.append("Hobart")
        elif num == 10:
            NameList.append("Alaskan Treasure")

    return NameList