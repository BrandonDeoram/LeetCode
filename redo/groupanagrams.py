from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]

globalList = defaultdict(list)

for word in strs:
    globalList[tuple(sorted(word))].append(word)

print(globalList.values())