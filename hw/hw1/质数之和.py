def judge_not_prime(a):
    result = False
    if a==2:
        return result
    else:    
        for i in range(2,a-1):
            if a%i==0:
                result = True
                break
    return result

N = input()
sum = 0
count = 0
number=2

while count<int(N):
    while judge_not_prime(number):
        number+=1
    sum+=number
    number+=1
    count+=1

print(sum)