


def repeatedSubstringPattern(s):
        len_s = len(s)
        for i in range(len_s//2):
            substring =s[:i+1]
            print(substring) 
            if substring*(len_s//len(substring)) == s:
                return True

s ="abaaba"
print(repeatedSubstringPattern(s))
# 3 times
# 12 letters
# 9/3 = 3 true , else its false

    
    
    
    

