import numpy as np
import pandas as pd
import random as rn
import copy
import math

def euc(i,j):
    d = len(i)
    dis = 0
    for k in range(d):
        dis+=(i[k]-j[k])**2
    return math.sqrt(dis)

def dist(data,centers):
    #k = len(centers)
    #d = len(data[0])
    clus = []
    for i in data:
        dis = []
        for j in centers:
            dis.append(euc(i,j))
        clus.append(np.argmin(dis))
    return clus
                       
    
def func(data,k):
    d = len(data[0])
    centers = []
    for i in range(k):
        x = copy.deepcopy(rn.choice(data))
        if x not in centers:
             centers.append(copy.deepcopy(x))
        else:
            while(x in centers):
                x = copy.deepcopy(rn.choice(data))
            centers.append(copy.deepcopy(x))
    p_centers = []
    temp = [0]*d
    for i in range(len(centers)):
        p_centers.append(copy.deepcopy(temp))
    recalc = False
    f = 1
    while f==1 or recalc:
        #print("while")
        #print(f)
        
        
        clus = dist(data,centers)
        # new centers
        p_centers = copy.deepcopy(centers)
        for i in range(k):
            t = [0]*d
            num=0
            for j in range(len(clus)):
                if i==clus[j]:
                    num+=1
                    for k in range(d):
                        t[k]+=data[j][k]
            for k in range(d):
                if num == 0:
                    recalc = True
                    print("Forced")
                else:
                    t[k]=(t[k]*1.0)/(float(num)*1.0)
            centers[i] = t
        #print(p_centers)
        #print(centers)
        #print()
        f = 0
        for i in range(len(centers)):
            for j in range(len(centers[i])):
                if centers[i][j] != p_centers[i][j]:
                    f=1
    
    return clus,centers
            
data = pd.read_csv("dt.csv").values
#data = [(1,1),(1.5,2),(2,2),(5,7),(5,5),(4.7,5),(6,6),(7,7)]
d = []
for i in data:
    d.append(list(i))
k = 3
clus,centers = func(d,k)
print("   ",clus)