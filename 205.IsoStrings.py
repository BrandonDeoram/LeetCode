def isIsomorphic(s, t):
# First initialize maps 
    sMap = {}
    tMap = {}

    #Iterate through s, t respectively
    for c1,c2 in zip(s,t):
        #Check to see if letter is in the map and if the letter ALREADY has a letter mapped to it 
        if((c1 in sMap and sMap[c1]!=c2) or (c2 in tMap and tMap[c2]!=c1)):
            return False
        # add characters to map
        sMap[c1] = c2
        tMap[c2] = c1
    return True