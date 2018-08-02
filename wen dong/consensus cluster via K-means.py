%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from sklearn.cluster import KMeans
import statsmodels.api as sm


def kmeans1(features,k):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(features)
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    list1=list(range(1000))
    return labels[:1000]

def kmeans2(D,k,dict2):
    kme=kmeans1(D,k)
    kme1=[]
    for i in dict2:
        a=dict2.index(i)
        kme1.append(kme[i[0]])
    return kme1

def meancon2(kind,resa,features):
    m=1000
    c=np.zeros([m,1])
    A=np.zeros([m,m])
    kk=kind
    distance1= pairwise_distances(features, metric='euclidean')
    dict2= kmeans1(distance1,kind)
    try1=conseq(dict2)
    for i in range(resa):
        refeatures=resample(features,i)
        D = pairwise_distances(features, metric='euclidean')
        c=kmeans2(D,kk,try1)     
        for l in range(0,m):
            for j in range(l+1,m):
                if c[l]==c[j]:
                    A[l][j]+=1
                    A[j][l]=A[l][j]
    con2=A/resa   
    return con2

def conseq(c):
    dict1={}
    for key in range(len(c)):
        if not key in dict1:
            dict1[key]=c[key]
    dict2= sorted(dict1.items(), key=lambda d:d[1]) 
    return dict2
 
def resample(feature,m):
    a1=feature[:(1000+10*m)]
    a2=feature[(1100+10*m):2000]
    a=np.row_stack((a1,a2))
    return a

def cdf(A,number=100,labels=''):
    list1=[]
    for i in range(len(A)):
        for j in range(i):
            list1.append(A[i][j])
    a=np.array(list1)
    ecdf = sm.distributions.ECDF(a)
    x = np.linspace(min(a), max(a),number)
    y = ecdf(x)
    plt.step(x, y,labels)

a=meancon2(5,50,features)
plt.imshow(a, interpolation='nearest')
plt.grid(True)
plt.colorbar()
plt.show()
p=cdf(a,10000)
    