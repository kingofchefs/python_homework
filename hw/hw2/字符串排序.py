def sort(a):
    a_sorted=''
    a_temp=[]
    for i in range(len(a)):
        a_temp.append(ord(a[i]))

    a_temp.sort()
    for i in range(len(a)):
        a_sorted+=chr(a_temp[i])
    return a_sorted


str_origin=input()
print(sort(str_origin.strip()))
