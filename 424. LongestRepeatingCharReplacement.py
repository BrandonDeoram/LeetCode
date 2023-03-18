def characterReplacement(s, k):
    res = 0
    count = {}
    l = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        # If valid window - max counter > k - 3-0 +1 4-2 = 2 > 1 shift the left window
        while((r-l+1)-max(count.values()) > k):
            l += 1
            count[s[r]] -= 1

    res = max(res, r-l+1)
    return res


print(characterReplacement(s="AABABBA", k=1))
