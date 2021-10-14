import os
import openpyxl
import shutil

def ReadExcel():
    print ("This May Take Awhile\n")
    DataSetPath = os.getcwd()
    DataSetPath = DataSetPath + "\Dataset\mozilla_core.xlsx"
    
    wb = openpyxl.load_workbook(DataSetPath)
    sheet = wb.active

    return sheet




def FilterResults():
    sheet = ReadExcel()
    Titles = sheet['E']
    NonFuncArr = []
    FuncArr = []
    SubStr1 = "not working"
    SubStr2 = "doesnt work"
    SubStr3 = "fail"
    SubStr4 = "Crash"
    SubStr5 = "Broken"
    SubStr6 = "doesn't work"
    SubStr7 = "dont work"
    SubStr8 = "don't work"

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
            elif SubStr5 in data.value:
                FuncArr.append(data.value)
            elif SubStr6 in data.value:
                FuncArr.append(data.value)
            elif SubStr7 in data.value:
                FuncArr.append(data.value)
            elif SubStr8 in data.value:
                FuncArr.append(data.value)
            else:
                NonFuncArr.append(data.value)
    


    #PerfArr = []
    #SubStr1 = "slow"
    #SubStr2 = "hung"
    #SubStr4 = "hanging"

    #for data in Titles:
    #    if type(data.value) is str:
    #        if SubStr1 in data.value:
    #            PerfArr.append(data.value)
    #        elif SubStr2 in data.value:
    #            PerfArr.append(data.value)
            #elif SubStr3 in data.value:
            #    PerfArr.append(data.value)
            #elif SubStr4 in data.value:
            #    PerfArr.append(data.value)


    #SecurArr = []
    #Titles2 = sheet['C']
    #i = 0

    #for data in Titles2:
    #    if type(data.value) is str:
    #        if data.value == 'Security':
    #            SecurArr.append(Titles[i].value)
    #    i = i + 1

    #print (len(SecurArr))
    #i = 0
    #for _ in range(10):
    #    print (SecurArr[i])
    #    i = i + 1
    return FuncArr, NonFuncArr


def WriteResults():
    FuncArr, NonFuncArr = FilterResults()
    
    DataPath = os.getcwd() + "\\Data"
    if (os.path.exists(DataPath)):
        shutil.rmtree(DataPath)
    os.mkdir(DataPath)

    DataPathFunc = os.getcwd() + "\\Data\\Functional"
    if (os.path.exists(DataPathFunc)):
        shutil.rmtree(DataPathFunc)
    os.mkdir(DataPathFunc)

    DataPathNonFunc = os.getcwd() + "\\Data\\Non-Functional"
    if (os.path.exists(DataPathNonFunc)):
        shutil.rmtree(DataPathNonFunc)
    os.mkdir(DataPathNonFunc)

    i = 0
    for x in FuncArr:
        StringChar = str(i)
        FileName = "FuncEx" + StringChar + ".txt"
        file1 = open(DataPathFunc + "\\" + FileName, "w+")
        file1.write(x)
        file1.close()
        i = i + 1

    i = 0
    stopint = 0
    for x in NonFuncArr:
        StringChar = str(i)
        FileName = "NonFuncEx" + StringChar + ".txt"
        file1 = open(DataPathNonFunc + "\\" + FileName, "w+")
        file1.write(x)
        file1.close()
        i = i + 1
        stopint = stopint + 1
        if (stopint == 20000):
            break




    #for x in FuncArr:
    return




if (__name__) == "__main__":
    WriteResults()