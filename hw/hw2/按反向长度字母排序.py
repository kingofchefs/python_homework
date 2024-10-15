def compare(ch1,ch2):
    res=True
    if len(ch1)>len(ch2):
        res=True
    elif len(ch1)<len(ch2):
        res=False
    else:
        for i in range(len(ch1)):
            if ord(ch1[i])>ord(ch2[i]):
                res=True
                break
            elif ord(ch1[i])<ord(ch2[i]):
                res=False
                break
    return res

def find_max(str):
    max=''
    for ch in str:
        if compare(ch,max):
            max=ch
    return max

def sort_1(str_in):
    str_in=str_in.split()
    ch_count=[]
    str_sorted=''
    for ch in str_in:
        if ch not in ch_count:
            ch_count.append(ch)
    while len(ch_count)!=0:
        max_ch=find_max(ch_count)
        str_sorted=str_sorted+max_ch+' '
        ch_count.remove(max_ch)
    return str_sorted

str_in=input()
print(sort_1(str_in))
        
    