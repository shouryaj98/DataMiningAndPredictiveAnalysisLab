import random
import math

def eucldist(p0,p1):
    dist = 0.0
    for i in range(0,len(p0)):
        dist += (p0[i] - p1[i])**2
    return math.sqrt(dist)


def kmeans(k,datapoints):
    d = len(datapoints[0]) 
    
    Max_Iterations = 1000
    i = 0
    
    cluster = [0] * len(datapoints)
    prev_cluster = [-1] * len(datapoints)
    
    cluster_centers = []
    for i in range(0,k):

        cluster_centers += [random.choice(datapoints)]
        force_recalculation = False
    
    while (cluster != prev_cluster) or (i > Max_Iterations) or (force_recalculation) :
        
        prev_cluster = list(cluster)
        force_recalculation = False
        i += 1

        for p in range(0,len(datapoints)):
            min_dist = float("inf")
            
            for c in range(0,len(cluster_centers)):
                
                dist = eucldist(datapoints[p],cluster_centers[c])
                
                if (dist < min_dist):
                    min_dist = dist  
                    cluster[p] = c   
        
        for k in range(0,len(cluster_centers)):
            new_center = [0] * d
            members = 0
            for p in range(0,len(datapoints)):
                if (cluster[p] == k): 
                    for j in range(0,d):
                        new_center[j] += datapoints[p][j]
                    members += 1
            
            for j in range(0,d):
                if members != 0:
                    new_center[j] = new_center[j] / float(members) 
                else: 
                    new_center = random.choice(datapoints)
                    force_recalculation = True
                    print ("Forced Recalculation...")
                    
            
            cluster_centers[k] = new_center
    
        
    print ("======== Results ========")
    print ("Clusters", cluster_centers)
    print ("Iterations",i)
    print ("Assignments", cluster)
    
    
datapoints = [(1,1),(1.5,2),(2,2),(5,7),(5,5),(4.7,5),(6,6),(7,7)]
k = 2
kmeans(k,datapoints) 

#dd = []
#f = open("k-data.csv")
#for i in f:
#    j = i.strip().split(",")
#    for k in range(len(j)):
#        j[k] = float(j[k])
#    dd.append(tuple(j))
#print(dd)
