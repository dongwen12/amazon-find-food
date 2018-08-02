import os
import pandas as pd
df1 = pd.read_csv('/Users/dongwen/Downloads/amazon-fine-food-reviews/Reviews.csv', encoding='gbk')
df2=df1[['Id','ProductId','UserId']]
df=df2.head(2000)
dict1={}
for key in range(len(df['Id'])):
    dict1[key+1]=df.iloc[key]
list1=[]
for p in range(len(df['Id'])):
    list1.append((dict1[p+1]['UserId'],dict1[p+1]['ProductId']))
ij_zeros = np.zeros((len(list(set(df['ProductId']))),len(list(set(df['UserId']))))) # 创建product*user的全0矩阵    
numj=0
for userj in list(set(df['UserId'])):
    numi=0
    for prodi in list(set(df['ProductId'])):
        if (userj,prodi) in list1:
            ij_zeros[numi][numj]=1
        numi=numi+1
    numj=numj+1
ii_zeros = np.zeros((len(list(set(df['ProductId']))),len(list(set(df['ProductId'])))))
i_ij_zeros=np.hstack((ii_zeros,ij_zeros))
ji_zeros=np.transpose(ij_zeros)
jj_zeros=np.zeros((len(list(set(df['UserId']))),len(list(set(df['UserId'])))))
j_ij_zeros=np.hstack((ji_zeros,jj_zeros))
features=np.vstack((i_ij_zeros,j_ij_zeros))
import seaborn as sns
from sklearn.metrics.pairwise import pairwise_distances
distance=1-np.corrcoef(features)
distance1 = pairwise_distances(features, metric='euclidean')
print(distance)

plt.imshow(features, interpolation='nearest')
plt.grid(True)
plt.colorbar()
plt.show()