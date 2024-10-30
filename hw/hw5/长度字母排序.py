sentence_raw=input().strip()
words=list(set(sentence_raw.split()))
words.sort(key=lambda x:(len(x),x))
print(' '.join(words))