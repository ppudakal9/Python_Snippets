def balance_par(s):
    if not len(s)%2 == 0:
        return False

    d = {')':'(', '}':'{', ']':'['}

    stack=[]
    i=0
    top=''
    while i < len(s):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        elif stack:
           top = stack.pop()
           if top != d[s[i]]:
               return False
        i+=1

    if not stack:
        return True

    return False


if balance_par("{[]}"):
    print("Is Valid")
else:
    print("Not Valid")