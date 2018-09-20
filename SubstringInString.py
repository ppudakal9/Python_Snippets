def isSubstring(text, pat):
    m = len(text)
    n = len(pat)

    if m < n:
        return False
    count = 0

    for i in range(0, m):
        if text[i: i+n] == pat:
            print(text[i:i+n])
            count+=1
            continue

    return count


#text = "ABECBBAEGHABABABBBABCRABCBBABBA"
text = "BBA"

pat = 'BBA'
print(isSubstring(text, pat))