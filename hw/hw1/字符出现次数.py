string=input().lower()
count=[0]*26
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
          'q','r','s','t','u','v','w','x','y','z']

for chara in string:
    for i in range(26):
        if chara==alphabet[i]:
            count[i]+=1

for i in range(26):
    print(count[i],end=' ')