num_bin=input()
num_dec=0
exponet=len(num_bin)-1

for i in num_bin:
    num_dec+=(int(i)*2**exponet)
    exponet-=1

print(num_dec)