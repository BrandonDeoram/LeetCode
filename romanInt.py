
s = "MCDLXXVI"
# 8


s = "III"
s = "MCMXCIV"
# 2
# Traverse throught the word

# Check to see if the number to the right is smaller current > next num if yes were good if no subtract move on
roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
         'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
newList = list(s)
total = 0

# two pointer
i = 0
j = 1
while(j != len(newList)+1):
    if(j >= len(newList)):
        total += roman.get(newList[i])
        break
    if(roman.get(newList[i]) >= roman.get(newList[j])):
        total += roman.get(newList[i])
        i += 1
        j += 1

    else:
        num = roman.get(newList[j])-roman.get(newList[i])
        total += num
        i = j+1
        j = i+1

print(total)
