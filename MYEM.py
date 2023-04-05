import csv
import numpy as np
from scipy import stats


# 数据初始化
pi = 0.7
u1 = 175
u2 = 160
Sig1 = 20
Sig2 = 20
height=[]

i=0
# 读取文件中数据
with open('./height_data.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    # skip the header
    next(csv_reader)
    for line in csv_reader:
      #np.array(height)=int(line[2])
      height.append(line[0])
      i=i+1

N=i
H=np.array(height,dtype=float)
P=np.zeros(N)

# 迭代数据赋初值，其中PD1、PD2为男女正态分布概率密度，P数组为每个数据属于男的概率
PD1 = 0
PD2 = 0
Psum = 0
Pxsum1 = 0
Pxsum2 = 0
numerator1 = 0
numerator2 = 0

# 迭代200次
for i in range(1,200):
    for cnt in range(0,N):

        PD1 = stats.norm.pdf(H[cnt],u1,Sig1)
        PD2 = stats.norm.pdf(H[cnt],u2,Sig2)

        P[cnt] = pi*PD1/(pi*PD1+(1-pi)*PD2)

    Psum = np.sum(P)
    Pxsum1 = np.dot(P,H)
    Pxsum2 = np.dot((1-P),H)

    pi = Psum/N

    u1 = Pxsum1/Psum
    u2 = Pxsum2/(N-Psum)
    #两个分子
    numerator1 = np.sum(np.dot(P,np.square(H-u1)))
    numerator2 = np.sum(np.dot((1-P),np.square(H-u2)))

    Sig1 = np.sqrt(numerator1/Psum)
    Sig2 = np.sqrt(numerator2/(N-Psum))
    Psum = 0
    Pxsum1 = 0 
    Pxsum2 = 0 
    numerator1 = 0
    numerator2 = 0
    
    P=np.zeros(N)

print("number:",N,"mean2:",u1,"mean1:",u2,"std2:",Sig1,"std1:",Sig2,"type choosing:",pi)

