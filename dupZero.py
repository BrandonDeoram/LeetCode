

from operator import le


arr = [0,0,0,0,0]
newArr = []
length = len(arr)
print(length)
counter=0
while(counter!=length):
    if(counter>length):
        break
    if(arr[counter] != 0):
        counter+=1
    else:
        arr.insert(counter+1,0)
        counter+=2
print(arr[:length])
