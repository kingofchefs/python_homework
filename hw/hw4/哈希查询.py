def hash_process(n,operations):
    data_set={}
    result=[]
    
    for operation in operations:
        t,x=operation
        if t==1:
            data_set.add(x)
        elif t==2:
            data_set.discard(x)
        elif t==3:
            result.append(1 if x in data_set else 0)
    return result

n=int(input())
operations=[tuple(map(int,input().split())) for _ in range(n)]

result=hash_process(n,operations)
for res in result:
    print(res)