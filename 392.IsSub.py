def isSubsequence(s, t):
    i=0
    j=0

    while(i < len(s) and j<len(t)):
        if(s[i]==t[j]):
            i+=1
        j+=1
    
    print(i,j)

    return i==len(s)

print(isSubsequence("ace","idk"))