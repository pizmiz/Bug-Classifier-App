import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import ManualLabel

def ImportData():
    PerfArr, FuncArr, SecurArr = ManualLabel.FilterResults()
    return PerfArr, FuncArr, SecurArr


def FormatData():
    PerfArr, FuncArr, SecurArr = ImportData()




    return PerfArr, FuncArr, SecurArr




def TrainModel():
    FormatData()


    
    return



if (__name__) == "__main__":
    TrainModel()