

s = "aacc"
t = "ccac"

# if(len(s) and len(t) <= 1 and len(s) == len(t)):
#     print('false')

# sList = list(s)
# tList = list(t)
# for x in sList:
#     if(sList.count(x) != tList.count(x)):
#         print('FALSE')
# print('true')

# HashMap Approach
if(s == t):
    print("true")
if(len(s) and len(t) <= 1 or len(s) != len(t)):
    print('false')
hashMapS = {}
hashMapT = {}

for x in s:
    if(x in hashMapS):
        count = hashMapS[x]
        hashMapS[x] = count+1

    else:
        hashMapS[x] = 1

for x in t:
    if(x in hashMapT):
        count1 = hashMapT[x]
        hashMapT[x] = count1+1

    else:
        hashMapT[x] = 1

print(hashMapS)
print(hashMapT)
print("FINAL", hashMapS == hashMapT)
