def compress_str(str_in):
    ch_count={}
    str_out=''
    for ch in str_in:
        if ch==' ':
            str_out+=ch
        else:
            if ch in ch_count:
                ch_count[ch]+=1
                if ch_count[ch] in [3,6]:
                    str_out+=ch
            else:
                ch_count[ch]=1
                str_out+=ch
    return str_out

str_in=input()
print(compress_str(str_in))