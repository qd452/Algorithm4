from collections import Counter, defaultdict
from sets import Set

literatureText = "i'm very good good good haha to is to to to to to"
wordsToExclude = ["to",]

literatureText = "rose is a flower rose is pond a flower rose flower in garden garden garden pond pond rose is a rose is a rose is a rose is a"
wordsToExclude = ["rose", "is", "a"]

def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]

def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    # WRITE YOUR CODE HERE
    rd = defaultdict(list)
    words = literatureText.split(' ')
    word_counter = Counter(words)
    for w_ex in wordsToExclude:
        del word_counter[w_ex]
    print(word_counter)
    for k,v in word_counter.items():
        rd[v].append(k)
    
    return rd[max(rd.keys())]


#rd = defaultdict(list)
#words = literatureText.split(' ')
#word_counter = Counter(words)
#for w_ex in wordsToExclude:
#    del word_counter[w_ex]
#print(word_counter)
#for k,v in word_counter.items():
#    rd[v].append(k)
    
    
finals = retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude)
print(finals)
#    
#words = literatureText.split(' ')
#word_counter = Counter(words)

####

from collections import Counter, defaultdict
from sets import Set

def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    rd = defaultdict(list)
    words = literatureText.split(' ')
    word_counter = Counter(words)
    for w_ex in wordsToExclude:
        del word_counter[w_ex]
    print(word_counter)
    for k,v in word_counter.items():
        rd[v].append(k)
    try:
        most_index = max(rd.keys())
    except:
        return None
    return rd[most_index]
