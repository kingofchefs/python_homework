sentence=input()
sentence=sentence.split()
word=[]
word_count=[]
sentence_out=''
for ch in sentence:
    if ch in word:
        word_count[word.index(ch)]+=1
        if word_count[word.index(ch)]<=2:
            ch_1=ch+ch+' '
            sentence_out+=ch_1
    else:
        word.append(ch)
        word_count.append(1)
        ch_1=ch+' '
        sentence_out+=ch_1
print(sentence_out.strip())