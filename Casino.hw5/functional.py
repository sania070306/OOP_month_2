import random

from decouple import config

MY_MONEY1 = config('MY_MONEY', cast = int)

def casino():
    while 1:
        global MY_MONEY1
        slot = int (input('Выберите слот '))
        bid = int (input('Сделайте ставку '))
        MY_MONEY1 -= bid
        winning_slot = random.randint(1,30)
        if slot == winning_slot:
            wining_money = bid * 2
        else:
            wining_money = 0
        MY_MONEY1 += wining_money
        question = input('do you want continued? \n y/n \n').lower()
        if question == 'n':
            print(MY_MONEY1)
            break
        else:
            continue

print(casino())
