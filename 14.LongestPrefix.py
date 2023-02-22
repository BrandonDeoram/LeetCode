def longestCommonPrefix(strs):
    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            if(len(s)== i or strs[0][i] != s[i][0]):
                return res
        res+=strs[0][i]
    return res


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
