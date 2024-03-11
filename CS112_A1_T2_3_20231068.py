#file : CS112_A1_T1_3_20231068
#Purpose : this program subtract a square game , the game start with number of coins that player need and only player takes a perfect square numbers , the last player who takes the last coin win
#Author: zyad atef al_abiad
#ID: 20231068

#  Representing the rules of the game to the players
print("to start the game you should enter the number of coins ")
print("the players must take a perfect square number of coins ")
print("the last player who takes the last coin wins ")
print("lets gooooo!")

#Getting the number of coins from user
Num_coins = int(input("please enter the number of coins: "))

import math
# Update the number of coins
def update_state(Coins_taken):
    global Num_coins
    Num_coins -= Coins_taken

# knowing the winner of yhe players
def is_winner():
    global Num_coins
    if Num_coins < 1:
        return True

while True:
    #for player 1
    subtracted_coin1 = int(input("player 1 please enter the number of coins to subtract: "))
    while subtracted_coin1 <= 0 or subtracted_coin1 % math.sqrt(subtracted_coin1) !=0  or subtracted_coin1 > Num_coins:
        subtracted_coin1 = int(input ( "invalid number ,please enter a perfect square number: ")) #to get true input
    update_state(subtracted_coin1)
    if is_winner():
        print("the first player won")
        break
    else:
        print("the reminder coins are:" , Num_coins)

        # for player 2
        subtracted_coin2 = int(input("player 2 please enter the number of coins to subtract: "))
    while subtracted_coin2 <= 0 or subtracted_coin2 % math.sqrt(subtracted_coin2) != 0 or subtracted_coin2 > Num_coins:
        subtracted_coin2 = int(input("invalid number ,please enter a perfect square number: "))  # to get true input
    update_state(subtracted_coin2)
    if is_winner():
        print("the second payer won")
        break
    else:
        print("the reminder coins are ",Num_coins)


