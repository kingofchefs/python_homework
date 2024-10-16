def judge_prime(a):
    result = True
    if a==2:
        return result
    else:    
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                result = False
                break
    return result

def fact(n):
    factor=set()
    for i in range(2,n+1):
        if n%i==0 and judge_prime(i):
            factor.add(i)
    return sorted(factor)

num=list(map(int, input().split()))
fact1=fact(num[0])
fact2=fact(num[1])

if fact1==fact2:
    for i in range(len(fact1)):
        print(fact1[i],end=' ')
else:
    for i in range(len(fact1)):
        print(fact1[i],end=' ')
    print('')
    for i in range(len(fact2)):
        print(fact2[i],end=' ')
