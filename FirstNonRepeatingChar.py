def firstNonRepeatingChar(s):
    nonrepeat_arr = []
    str_arr = []

    for c in s:
        if c not in str_arr:
            str_arr.append(c)
            nonrepeat_arr.append(c)
        else:
            nonrepeat_arr.remove(c)

    if nonrepeat_arr:
        return nonrepeat_arr[0]
    else:
        return '_'


print(firstNonRepeatingChar("abachfolj"))
print(firstNonRepeatingChar("aabbcdsdcs"))