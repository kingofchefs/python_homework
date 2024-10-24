morse={
    '.-':'A',
    '-...':'B',
    '-.-.':'C',
    '-..':'D',
    '.':'E',
    '..-.':'F',
    '--.':'G',
    '....':'H',
    '..':'I',
    '.---':'J',
    '-.-':'K',
    '.-..':'L',
    '--':'M',
    '-.':'N',
    '---':'O',
    '.--.':'P',
    '--.-':'Q',
    '.-.':'R',
    '...':'S',
    '-':'T',
    '..-':'U',
    '...-':'V',
    '.--':'W',
    '-..-':'X',
    '-.--':'Y',
    '--..':'Z'
}

def morse_to_english(sentence_raw):
    sentence=[]
    words_raw=sentence_raw.split('  ')
    
    for word_raw in words_raw:
        letters=word_raw.split(' ')
        word=''.join(morse[letter] for letter in letters)
        sentence.append(word)
    
    return ' '.join(sentence)

sentence_raw=input()
print(morse_to_english(sentence_raw))