def if_anagram(word1,word2):
    return sorted(word1)==sorted(word2)

def examine(sentence,key_words):
    res_examined=[]
    for word in sentence:
        for key_word in key_words:
            if if_anagram(word,key_word):
                res_examined.append(key_word)

    return res_examined

key_words=input().split()
sentence=input().split()

#print(' '.join(examine(sentence,key_words)))
for x in examine(sentence,key_words):
    print(x,end=' ')