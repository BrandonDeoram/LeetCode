from collections import Counter, defaultdict


def groupAnagrams(strs):
    letters_to_words = defaultdict(list)
    for word in strs:
        letters_to_words[tuple(sorted(word))].append(word)
    return list(letters_to_words.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(groupAnagrams(strs))

t1 = tuple('atea')
t2 = tuple('eat')

print(list(t1).sort())
