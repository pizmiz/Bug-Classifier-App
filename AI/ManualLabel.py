import os
import openpyxl


def ReadExcel():
    DataSetPath = os.getcwd()
    DataSetPath = DataSetPath + "\Dataset\mozilla_core.xlsx"
    
    wb = openpyxl.load_workbook(DataSetPath)
    sheet = wb.active

    return sheet




def FilterResults():
    sheet = ReadExcel()
    Titles = sheet['E']
    FuncArr = []
    SubStr1 = "not working"
    SubStr2 = "Not Working"
    SubStr3 = "fail"
    SubStr4 = "Crash"

    for data in Titles:
        if type(data.value) is str:
            if SubStr1 in data.value:
                FuncArr.append(data.value)
            elif SubStr2 in data.value:
                FuncArr.append(data.value)
            elif SubStr3 in data.value:
                FuncArr.append(data.value)
            elif SubStr4 in data.value:
                FuncArr.append(data.value)
    


    PerfArr = []
    SubStr1 = "slow"
    SubStr2 = "hung"
    #SubStr4 = "hanging"

    for data in Titles:
        if type(data.value) is str:
            if SubStr1 in data.value:
                PerfArr.append(data.value)
            elif SubStr2 in data.value:
                PerfArr.append(data.value)
            #elif SubStr3 in data.value:
            #    PerfArr.append(data.value)
            #elif SubStr4 in data.value:
            #    PerfArr.append(data.value)


    SecurArr = []
    Titles2 = sheet['C']
    i = 0

    for data in Titles2:
        if type(data.value) is str:
            if data.value == 'Security':
                SecurArr.append(Titles[i].value)
        i = i + 1

    #print (len(SecurArr))
    #i = 0
    #for _ in range(10):
    #    print (SecurArr[i])
    #    i = i + 1
    return PerfArr, FuncArr, SecurArr




if (__name__) == "__main__":
    FilterResults()