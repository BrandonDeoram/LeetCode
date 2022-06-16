


s = "dvdf"
l = 0
maxLen = 0
hashSet = set()
for r in range(len(s)):
    while(s[r] in hashSet):
        hashSet.remove(s[l])
        l+=1
    hashSet.add(s[r])
    maxLen =max(len(hashSet),maxLen)

print(maxLen)



# abcab