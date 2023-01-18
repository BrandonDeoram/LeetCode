from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    if(len(s) != len(t)):
        return False

    hashMaps = Counter(s)
    hashMapt = Counter(t)
    print(hashMaps)
    return True if hashMaps == hashMapt else False


print(isAnagram("anagram", "nagaram"))
