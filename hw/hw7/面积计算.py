import math

def area(op,parameter):
    if op=='0':
        res=parameter[0]**2
    elif op=='1':
        res=parameter[0]*parameter[1]
    elif op=='2':
        p=(parameter[0]+parameter[1]+parameter[2])/2
        res=math.sqrt(p*(p-parameter[0])*(p-parameter[1])*(p-parameter[2]))
    elif op=='3':
        res=math.pi*parameter[0]**2

    return res

op=input()
parameter=list(map(float,input().split()))
res=area(op,parameter)

print('%.2f' %res)