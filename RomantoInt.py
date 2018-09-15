def roman_to_int(s):
    #define a dict of roman numerals
    dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    res=0
    i = 0
    while i < len(s):
        if(i < len(s)-1 and dict[s[i]] < dict[s[i+1]]):
            res+= dict[s[i+1]] - dict[s[i]]
            i = i + 2
        else:
            res+=dict[s[i]]
            i = i + 1

    print(res)


roman_to_int("IV")