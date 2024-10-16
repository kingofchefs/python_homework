def arrange(num):
    if len(num)==1:
        return [num]
    res = []
    for i in range(len(num)):
        current = num[i]
        num_temp = num[:i] + num[i+1:]
        for res_temp in arrange(num_temp):
            res.append([current] + res_temp)
    return res

N=int(input())
res=arrange(list(range(1,N+1)))

for i in res:
    print(' '.join(map(str, i)))