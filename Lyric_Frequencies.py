"""
Lyric Frequency
Author - @Antriksh_Sharma
Date - 06/07/2018
MITx - Edx Course - Computer Science
Python 3.6

"""
lyrics = input('Enter the lyrics: ')
lyrics = lyrics.split()

def freq(lyrics):
    Frequencies = {}
    for word in lyrics:
        if word in Frequencies:
            Frequencies[word] += 1
            
        else:
            Frequencies[word] = 1
            
        
    return Frequencies

frequency = freq(lyrics)    

def mostComWord(frequency):
    values = frequency.values()
    best = max(values)
    words = []
    for i in frequency:
        if frequency[i] == best:
            words.append(i)
    return (words, best)

def most_common(freq, minm):
    result = []
    checker = False    
    while not checker:
        temp = mostComWord(freq)
        if temp[1] >= minm:
            result.append(temp)
            for w in temp[0]:
                del(freq[w])
        else:
            checker = True
    return result

print(most_common(frequency, 4))
