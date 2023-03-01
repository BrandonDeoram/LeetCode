def firstPalindrome(words):
    for s in words:
        if(s[::-1] == s):
            return s
    return ""
words = ["abc","car","ada","racecar","cool"]

print(firstPalindrome(words=words))