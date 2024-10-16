numbers=[]

while True:
    num=int(input())
    if num==0:
        break
    else:
        numbers.append(num)

numbers.sort()

for i in range(len(numbers)):
    print(numbers[i],end=' ')