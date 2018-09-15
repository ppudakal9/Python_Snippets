def cartProduct(lists):
    results = [[]]

    for i in range(0, len(lists)):
        curr_list = lists[i]
        temp = []
        for j in range(0, len(results)):
            for k in range(0, len(curr_list)):
                results[j] +=curr_list[k]
                temp.append(results[j])

        results = temp

    return results

a = [ [ 'a', 'b' ], [ 'c', 'd', 'e' ], [ 'f', 'g' ] ]
print(cartProduct(a))