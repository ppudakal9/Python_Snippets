#using memoization : cache
def ways_to_decode(str, str_len, cache):
    if str_len  == 0:
        return 1

    index = len(str) - str_len
    if str[index] == '0':
        return 0

    if cache[str_len] is not None:
        return cache[str_len]

    numOfWays = ways_to_decode(str, str_len-1, cache)
    if str_len >= 2 and int(str[index:index+2]) <= 26:
        numOfWays += ways_to_decode(str, str_len-2, cache)

    cache[str_len] = numOfWays
    return numOfWays


def decode_ways(str):
    cache = [None]*(len(str)+1)
    str_len = len(str)
    return ways_to_decode(str, str_len, cache)


print(decode_ways("226"))