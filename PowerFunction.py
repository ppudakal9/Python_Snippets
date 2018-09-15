def pow(a, n):
    if n == 0:
        return 1.0

    if n < 0:
        n = -n
        a = 1/a 

    x = pow(a, int(n/2))

    res=1
    if n % 2 == 0:
        res = x*x
    else:
        res = a*x*x

    return res


n=-2.00000
a=-2147483648
result = pow(a, n)
print(result)
#if n < 0:
 #   print(1/result)
#else:
 #   print(result)