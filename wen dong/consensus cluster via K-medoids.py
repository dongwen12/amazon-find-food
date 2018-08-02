%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import numpy as np
import random

def kMedoids(D, k, tmax=1000):
    # determine dimensions of distance matrix D
    m, n = D.shape

    if k > n:
        raise Exception('too many medoids')
    # randomly initialize an array of k medoid indices
    M = np.arange(n)
    np.random.shuffle(M)
    M = np.sort(M[:k])

    # create a copy of the array of medoid indices
    Mnew = np.copy(M)

    # initialize a dictionary to represent clusters
    C = {}
    for t in range(tmax):
        # determine clusters, i. e. arrays of data indices
        J = np.argmin(D[:,M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J==kappa)[0]
        # update cluster medoids
        for kappa in range(k):
            
            J = np.mean(D[np.ix_(C[kappa],C[kappa])],axis=1)
            if len(J) > 0:
                j = np.argmin(J)
                Mnew[kappa] = C[kappa][j]
        np.sort(Mnew)
        # check for convergence
        if np.array_equal(M, Mnew):
            break
        M = np.copy(Mnew)
    else:
        # final update of cluster memberships
        J = np.argmin(D[:,M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J==kappa)[0]
    list1=list(range(1000))
    for key in C:
        for i in range(len(C[key])):
            if C[key][i]<=1000:
                list1[C[key][i]-1]=key
    #return C
    return list1

def resample(feature,m):
    a1=feature[:(1000+10*m)]
    a2=feature[(1100+10*m):2000]
    a=np.row_stack((a1,a2))
    return a

def conseq(c):
    dict1={}
    for key in range(len(c)):
        if not key in dict1:
            dict1[key]=c[key]
    dict2= sorted(dict1.items(), key=lambda d:d[1]) 
    return dict2 

def kMedoids1(D, k,dict2, tmax=1000):
    kme=kMedoids(D,k,tmax)
    kme1=[]
    for i in dict2:
        a=dict2.index(i)
        kme1.append(kme[i[0]])
    return kme1

def con2(kind,resa,features):
    m=1000
    c=np.zeros([m,1])
    A=np.zeros([m,m])
    kk=kind
    distance1=np.ones(np.shape(features))-np.corrcoef(features)
    dict2= kMedoids(distance1,kind)
    try1=conseq(dict2)
    for i in range(resa):
        refeatures=resample(features,i)
        D =1-np.corrcoef(refeatures)
        c=kMedoids1(D,kk,try1)
        for l in range(0,m):
            for j in range(l+1,m):
                if c[l]==c[j]:
                    A[l][j]+=1
                    A[j][l]=A[l][j]
    con2=A/resa   
    return con2

a=con2(3,50,features)
len(a)

plt.imshow(a, interpolation='nearest')
plt.grid(True)
plt.colorbar()
plt.show()