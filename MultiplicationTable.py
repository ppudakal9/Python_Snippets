def multiplication(y):
    # i = 0
    # j = 1
    # while (i < y ):
    #     print(x*j)
    #     i+=1
    #     j+=1
    r = 1
    c = 1
    while (r < y+1):
        for i in range(1, c+1):
            print(r*i, end = ' ')

        print()
        c+=1
        r+=1


multiplication(6)