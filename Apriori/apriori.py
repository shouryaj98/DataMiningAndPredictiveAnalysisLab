import copy
def prune(c,mins):
    cc = dict()
    for i in c:
        if c[i]>=mins:
            cc[i] = c[i]
    return cc

def gen(l):
    c = dict()
    lis = sorted(l.keys())
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if lis[i][:-1]==lis[j][:-1]:
                t = lis[i]+(lis[j][-1],)
                c[t] = 0
    return c

def cand_freq(c,name):
    f = open(name)
    for i in f: 
        for k in c:
            num = 0
            for l in k:
                if l in i.strip().split(","):
                    num+=1
            if num == len(k):
                c[k] += 1
    return c            
    
name = "ex1.csv"
mins = 3 #min_support

f = open(name)
c1 = dict()
for i in f:
    for j in i.strip().split(","):
        if (j,) not in c1:
            c1[(j,)] = 1
        else:
            c1[(j,)] += 1
f.close()
            
print("c 1- ",c1)
cp = copy.deepcopy(c1)
l = prune(c1,mins)
print("l 1",l)
countt = 2
while l != {}:
    c = gen(l)
    c = cand_freq(copy.deepcopy(c),name)
    print("c",countt,"- ",c)
    l = prune(c,mins)
    print("l",countt,"- ",l)
    countt+=1
    
    

    
        