s = ""

# sub j exclusive so +1
i = 0
j = 1
maxLen = float('-inf')
maxSub = ""
currSub = ""
# print(s[i:j+1])

while(j < len(s)):

    print(currSub)
    if(s[i] == s[j]):
        currSub = s[i:j+1]
        maxLen = max(len(currSub), maxLen)
        j += 1
    else:
        i = j
        j += 1
if(maxLen<=0):
    maxLen=1
print(maxLen)
