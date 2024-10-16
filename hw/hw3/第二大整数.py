numbers=[]
while True:
    num=int(input())
    if num==0:
        break
    else:
        numbers.append(num)
numbers=list(set(numbers))
numbers.sort()
print(numbers[-2])