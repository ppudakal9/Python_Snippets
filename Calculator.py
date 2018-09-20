#expression = "6+9-12" result = 3

import re

def calculator(exp):

    def add(a, b):
        return a+b

    def sub(a, b):
        return a-b

    p = re.split("([+-/*])", exp)
    print(p)

    nums = []
    oper = []

    for s in range(0, len(p)):
        if p[s].isdigit():
            nums.append(int(p[s]))
        elif p[s] == '+' or p[s] == '-':
            oper.append(p[s])
    print(nums, " ", oper)

    nums_index = 0
    res = 0

    for i in oper:
        if i == '+':
            res = add(nums[nums_index], nums[nums_index+1])
            nums_index = nums_index + 2
        elif i == '-':
            res = sub(res, nums[nums_index])
            nums_index = nums_index+1

    print(res)


calculator("6+9-12")