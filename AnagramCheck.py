def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    alphabet = [0]*26

    for i in range(0, len(s1)):
        index = ord(s1[i]) - ord('a')
        alphabet[index]+= 1

    for j in range(0, len(s2)):
        index = ord(s2[j]) - ord('a')
        alphabet[index]-= 1

    for count in alphabet:
        if count != 0:
            return False

    return True

def anagramCheck(s1, s2):
    if len(s1) != len(s2):
        return False

    alphabet = {}

    for i in range(0, len(s1)):
        x = s1[i]
        if x in alphabet:
            alphabet[x] += 1
        else:
            alphabet[x] = 1

    for j in range(0, len(s2)):
        y = s2[j]
        if y in alphabet:
            alphabet[y] -= 1
        else:
            return False

    for v in alphabet.values():
        if v!=0:
            return False

    return True

s = "anagram"
t = "nagaram"
print("Using array of size 26:", isAnagram(s, t))

print("Using dictionary:", anagramCheck(s, t))