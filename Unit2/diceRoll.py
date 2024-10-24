import random

play = int(input("Play - 1 \n "
                 "Quit - 0 \n Enter your choice: "))

if play == 1:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    print(dice1, dice2, dice3)

    if dice1 == dice2 and dice1 == dice3:
        print("Jackpot! - 1000 points")
    elif dice1 == dice2 or dice1 == dice3 or dice2 == dice3:
        print("100 points!")
    else:
        print("0 points")
