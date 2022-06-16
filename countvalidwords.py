
import string
import re
sent = "cat and  dog"
"  "
# Expected output should 3

# Break each word down into token put into list
sent1 = " ".join(sent.split())
sen_list = sent1.split(" ")
counter = 0
hyphencount = 0

# Iterate over each word and look into their chars

valid = True
print(sen_list)
for x in range(len(sen_list)):

    if(sen_list[x].islower):
        if("-" in sen_list[x]):
            index = sen_list[x].find("-")
            word = list(sen_list[x])
            diffcount = word.count(string.punctuation)
            print("ENTERED - zone", word)
            if(word[index+1] == word[index].islower() and word[index-1] == word[index].islower() and diffcount <= 1):
                # its valid a-b
                print('enters')
                counter += 1
            else:
                print('breaks')
                break
        elif("!", ".", "," in sen_list[x]):
            print("entered punctioan ", sen_list[x])
            word = list(sen_list[x])
            if(string.punctuation in word[0] and len(word)>1):
                print('somthingis worng')
                continue
            else:
                print("word is good", sen_list[x])
                counter += 1
        else:
            print("entered else word:\n")
            print(sen_list[x])
            counter += 1

print(counter)
'''
 - Check if each sentence contains only lowercase letters, hypens or punc BUT NO DIGITS
 - Check if a word contains a hyphen it should only be surrounded with letters before and after (between) if - if first or last index its invalid
 - If punct is present must be last
'''
