import pandas as pd
import math 
import numpy as np
import copy

def get_freq_dict(data,ind):
    dic = dict()
    for row in range(len(data)):
        if data[row][ind] not in dic:
            dic[data[row][ind]] = 1
        else:
            dic[data[row][ind]] += 1
    return dic
            
def most(data):
    dic = get_freq_dict(data,0)
    ma = -1
    ind = ''
    for i in dic:
        if dic[i]>ma:
            ma = dic[i]
            ind = i
    return ind

def purity(data):
    lis = []
    for row in data:
        if row[0] not in lis and len(lis)>0:
            return 0,0
        if row[0] not in lis:
            lis.append(row[0])
        else:
            pass
    return 1,lis[0]

def info_d(data):
    dic = get_freq_dict(data,0)
    total = 0
    summ = 0
    for i in dic:
        total+=dic[i]
    for i in dic:
        summ+=(dic[i]/total)*math.log2(dic[i]/total)
    return summ*(-1)

def split_attri(data,col,val):
    lis = []
    for row in data:
        if row[col] == val:
            dup = list(copy.deepcopy(row))
            del dup[col]
            lis.append(dup)
    return lis
            
def info_attri(data,col):
    dic = get_freq_dict(data,col)
    total = 0
    for i in dic:
        total+=dic[i]
    dic2 = dict()
    for i in dic:
        dic2[i] = split_attri(data,col,i)
    summ = 0
    for i in dic:
        summ+=(dic[i]/total)*info_d(dic2[i])
    return summ
    
def func(data):
    if len(data)==0:
        return 0
    if len(data[0])<=2:
        #print("func-2")
        return most(data)
    pure,label = purity(data)
    if pure==1:
        #print("func-3")
        return label
    #print("func-")
    info = info_d(data)
    info_attr = [0]*len(data[0])
    for i in range(1,len(data[0])):
        info_attr[i] = info_attri(data,i)
    gain = [0]*len(data[0])
    for i in range(1,len(data[0])):
        gain[i] = info - info_attr[i]
    max_in = np.argmax(gain)
    dic = get_freq_dict(data,max_in)
    dic2 = dict()
    for i in dic:
        dic2[i] = split_attri(data,max_in,i)
    dic3 = dict()
    for i in dic2:
        dic3[str(max_in)+'_'+str(i)] = func(dic2[i])
    return dic3

data = pd.read_csv("dt.csv").values
print(data)
tree = func(data)
print(tree)
        
    
