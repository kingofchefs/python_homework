count=[0]*3

while True:
    line=input()
    
    if '#' in line:
        line=line.split('#')[0]
        for c in line:
            if c==' ':
                count[0]+=1
            else:
                count[2]+=1
        break
    else:
        count[1]+=1
        for c in line:
            if c==' ':
                count[0]+=1
            else:
                count[2]+=1

for counter in count:
    print(counter, end=" ")


