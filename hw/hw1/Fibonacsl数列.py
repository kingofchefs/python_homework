def Fibonacsi(F_1,F_2,a,b,n):
    if n==1:
        return F_1
    elif n==2:
        return F_2
    elif n>2:
        return a*Fibonacsi(F_1,F_2,a,b,n-2)+b*Fibonacsi(F_1,F_2,a,b,n-1)

parameter=input().split()
parameter=[int(num) for num in parameter]

print(Fibonacsi(parameter[0],parameter[1],parameter[2],parameter[3],parameter[4]))