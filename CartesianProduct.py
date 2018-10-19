def cartProduct(lists):
    results = []
    for i in lists[0]:
        results.append(i)

    for i in range(1, len(lists)):
        curr_list = lists[i]
        temp = []
        for j in range(0, len(results)):
            for k in range(0, len(curr_list)):
                #results[j]+=(curr_list[k])
                temp.append(results[j]+curr_list[k])

        results = temp

    return results

a = [ [ 'a', 'b' ], [ 'f', 'g' ], ['c', 'd'] ]
print(cartProduct(a))

#['afc', 'afd', 'agc', 'agd', 'bfc', 'bfd', 'bgc', 'bgd']