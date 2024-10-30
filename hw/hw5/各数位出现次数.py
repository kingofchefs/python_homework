def multiply(a,b):
    c=[0]*(len(a)+len(b))
    for i in range(len(a)):
        for j in range(len(b)):
            res=a[i]*b[j]
            c[i+j]+=res%10
            c[i+j+1]+=res//10

    for i in range(len(c)-1):
        c[i+1]+=c[i]//10
        c[i]%=10
    
    while len(c) > 1 and c[-1] == 0:
        c.pop()

    return c

def change(n):
    return list(map(int, str(n)))[::-1]

def factorial(n):
    if n==0 or n==1:
        return [1]
    else:
        return multiply(change(n),factorial(n-1))
    
n=int(input())
res=factorial(n)
result={
    i:0 for i in range(10)
}
for i in res:
    result[i]+=1

for key in range(10):
    print(result[key],end=' ')