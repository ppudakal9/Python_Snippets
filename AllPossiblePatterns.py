#Given a string as input, return the list of all the patterns possible:

#'1' : ['A', 'B', 'C'],
#'2' : ['D', 'E'],
#'12' : ['X']
#'3' : ['P', 'Q']
#Example if input is '123', then output should be [ADP, ADQ, AEP, AEQ, BDP, BDQ, BEP, BEQ, CDP, CDQ, CEP, CEQ, XP, XQ]

def all_possible_patterns(str, res):

    if str == '':
        print(res)
        return
    for i in range(1, len(str)+1):
        temp=str[:i]
        if temp in d.keys():
            for item in d[temp]:
                all_possible_patterns( str[i:], res+item)


d = {'1': ['A', 'B', 'C'], '2': ['D', 'E'], '12': ['X'], '3': ['P', 'Q']}
str = "123"
res = ' '
all_possible_patterns(str, res)

