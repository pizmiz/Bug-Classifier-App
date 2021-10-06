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
    SubStr3 = "failed"
    SubStr4 = "Failed"

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
    

    print (len(FuncArr))
    i = 0
    for _ in range(10):
        print (FuncArr[i])
        i = i + 1
    return




if (__name__) == "__main__":
    FilterResults()