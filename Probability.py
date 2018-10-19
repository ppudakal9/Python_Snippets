from random import *

def cal_prob():
    red = 0
    black = 0
    balance = 100
    color = randint(0,1)
    while(balance > 0 and balance < 200) :
        if color == 0:
            red+=1
            black=0
        elif color == 1:
            black+=1
            red=0

        color = randint(0,1)

        if red == 4:
            red = 0
            black = 0
            if color == 1:
                balance+=10

            else:
                balance-=10
                red=0
        elif black == 4:
            red = 0
            black = 0
            if color == 0:
                balance+=10
            else:
                balance-=10
        else:
            continue

    print('bal=',balance)
    if balance == 200:
        return 1
    else:
        return 0


win = 0
lose = 0

for i in range(0, 100):
    ret = cal_prob()
    if ret==1:
        win+=1
    else:
        lose+=1
print(win)