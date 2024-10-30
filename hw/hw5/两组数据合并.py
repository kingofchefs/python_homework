m,n=map(int, input().split())

data1=[]
data2=[]

data1_raw=input().split()
data2_raw=input().split()

for i in range(m):
    data1.append(int(data1_raw[i]))
for i in range(n):
    data2.append(int(data2_raw[i]))

data=sorted(set(data1+data2))

for i in data:
    print(i,end=' ')