s = "badc"
t = "baba"

i = 0
j = 1
sList = []
tList = []
# Sliding window for s

while(j < len(s)):
    if(s[i] == s[j]):
        j += 1
    else:
        n = len(s[i:j])
        sList.append(n)
        i = j
        j += 1
sList.append(len(s[i:j]))
i=0
j=0
# Sliding window for t
while(j < len(s)):
    if(t[i] ==t[j]):
        j += 1
    else:
        n = len(t[i:j])
        tList.append(n)
        i = j
        j += 1
tList.append(len(t[i:j]))
print(sList.__eq__(tList))
# Compare both list
