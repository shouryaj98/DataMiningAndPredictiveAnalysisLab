# Without using any external library 
# Only works for dataset having categorical attributes and the first column is the class label
import math
import copy
import csv
def get_freq_dict(data,col):
    #to find freq of each unique attribute in a col and return as a dict
    dic = dict()
    for i in data:
        if i[col] not in dic:
            dic[i[col]] = 1
        else:
            dic[i[col]] += 1
    return dic
    
def most(data):
    # used to find the class with highest freq
    dic = get_freq_dict(data,0)
    maxx = -1
    ind = -1
    for i in dic:
        if dic[i] > maxx:
            maxx = dic[i]
            ind = i
    return ind

def info_d(data):
    # to find info_d of dataset
    dic = get_freq_dict(data,0) 
    tot = 0
    summ = 0
    for i in dic:
        tot += dic[i]
    for i in dic:
        summ += (dic[i]/tot)*math.log2(dic[i]/tot)
    summ = summ*(-1)
    return summ
        
def split_attr(data,col,j):
    # to split the dataset based on a particular attri
    lis = []
    for row in data:
        if row[col] == j:
            dup = copy.deepcopy(row)
            del dup[col]
            lis.append(dup)
    return lis
        
    
def func_info_attr(data,col):
    # to find the info of a particular attribute
    dic = get_freq_dict(data,col)
    tot = 0
    summ = 0
    for i in dic:
        tot += dic[i]
    
    dic2 = dict()
    for j in dic:
        dic2[j] = split_attr(data,col,j)
    for j in dic2:
        info_j = info_d(dic2[j])
        summ +=(dic[j]/tot)*info_j
    return summ
        
def pure(data):
    # to check if dataset is pure or not
    li = []
    for row in data:
        #print(row)
        if row[0] in li:
            pass
        else:
            li.append(row[0])
    if len(li) == 1:
        return 1,li[0]
    else:
        return 0,-1
        
def func(data):
    if len(data) == 0:
        return 0
    if len(data[0]) <= 2 :
        return most(data)
    purity,label = pure(data)
    if purity == 1:
        return label
    
    infod = info_d(data)
    no_attri = len(data[0])
    info_attri = []
    for i in range(1,no_attri):
        info_attri.append(func_info_attr(data,i))
    gain = []
    for i in range(1,no_attri):
        gain.append(infod-info_attri[i-1])
    maxx = -1
    ind = -1
    for i in range(len(gain)):
        if(gain[i]>maxx):
            maxx = gain[i]
            ind = i+1
    dic = get_freq_dict(data,ind)
    dic2 = dict()
    for i in dic:
        dic2[i] = split_attr(data,ind,i)
    dic3 = dict()
    for i in dic:
        dic3[str(ind)+'_'+str(i)] = func(dic2[i])
    return dic3
        
        
def readData(filename):
	reader = csv.reader(open(filename, 'r'))
	transactions = []
	for row in reader:
		transactions.append(row)
	return transactions
    
#data = [['a','c','f','j'],
#        ['b','c','f','j'],
#        ['b','e','h','k'],
#        ['a','c','f','i']
#        ]

data = readData('dt.csv')

tree = func(data)
print(tree)