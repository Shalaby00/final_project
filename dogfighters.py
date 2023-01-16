import sys
import re
import time
import math
import random

game_over = False
easy_mode = False
hard_mode = False
pvp_mode = False

class Foe():
    # each plane is an object, stats can be passed through different functions
    def __init__(self):

        self.name= 'FW-190'
        self.s=700
        self.c=15
        self.a=500
        self.m=1

        self.l= self.a
        self.h=1200
        self.v=400
class P47():
    def __init__(self):

        self.name= 'You'
        self.s=700
        self.c=11
        self.a=3400
        self.m=3

        self.l= self.a
        self.h=2000
        self.v=400
class P51():
    def __init__(self):
        self.name= 'You'
        self.s=698
        self.c=18
        self.a=2080
        self.m=2

        self.l= self.a
        self.h=1800
        self.v=400
class Spitfire():
    def __init__(self):
        self.name= 'You'
        self.s=650
        self.c=20
        self.a=1640
        self.m=1

        self.l= self.a
        self.h=1700
        self.v=400
class La7():
    def __init__(self):
        self.name= 'You'
        self.s=670
        self.c=18
        self.a=340
        self.m=0.25

        self.l= self.a
        self.h=1900
        self.v=400

def main():
    # each global variable represents a game setting that can be tripped by any function, effecting the entirety of the game.
    global game_over
    global easy_mode
    global hard_mode
    global pvp_mode
    intro()
    # this code enables for choosing tutorial settings, pvp modes, and game mode./////////////////
    tut= tutorial_choice()
    if (tut == 2):
        tutorial()
    pvp()
    mode = choose_mode()
    if (mode==1):
        easy_mode = True
    if (mode==3):
        hard_mode = True
    player1 = choose_plane()
    if pvp_mode == False:
        player2 = Foe()
    else:
        print("\nPlayer2:")
        player2 = choose_plane()
    print("\nStarting Game")
    # sets up a loding screen
    for i in range(10):
        loading_screen()
    # establishes turns, up until 100
    for i in range(100):
        # if the game ends before the turn starts, this loop is broken
        if game_over:
            print("Game Over")
            break
        # player1 turn
        print("\n\nPlayer 1, Turn:", i+1, "------------------------------------------------------------------")
        turn(player1, player2)
        time.sleep(3)
        # if the game ends midway through a turn, this loop is broken
        if game_over:
            break
        # in single player, the computer takes it's turn
        if (pvp_mode==False):
            opponent(player2, player1)
        # in pvp mode, player 2 takes a turn
        else:
            print("Player 2: -----------------------------------------------------------------")
            turn(player2, player1)
        time.sleep(3)
        # if the game ends at the end of the turn, this loop is broken
        if game_over:
            break

def turn(player, player2):
    global game_over
    global easy_mode
    # rounds your position, ammo, and speed, as to stop round - off errors
    print_options(math.floor(player.h), math.floor(player.v), math.floor(player.l))
    # in easy mode the rough position of the enemy is revealed
    if(easy_mode == True):
        if(player.h > player2.h):
            print("The enemy is below you.")
        if(player.h < player2.h):
            print("The enemy is above you.")
        if(player.h == player2.h):
            print("The enemy is at the same altitude.")
    # makes sure card selections are valid, reprompts for input if they're not
    while True:
        try:
            choice = int(input("Maneuver:"))
        except ValueError:
            print("Please use a number from 1-9")
            continue
        if choice > 9 or choice < 1:
            print("Please use a number from 1-9")
            continue
        else:
            break
    # if the player decides to quit, the game is ended, else they choose their cards.
    if (choice == 9):
        print("You Quit\n")
        game_over=True
        outro()
    else:
        cards(player, player2, choice)
        if flight(player) > 0:
            game_over=True
            outro()
    return 0

def opponent(player, player2):
    global game_over
    # the opponents chances of playing certain cards are dependent on the following wieghts, each representing a span of numbers from 1 - 100.
    roll=random.randint(1,100)
    froll=0
    if 0 < roll < 25:
        froll = 3
    if 24 < roll < 47:
        froll = 2
    if 46 < roll < 53:
        froll = 5
    if 52 < roll < 55:
        froll = 6
    if 54 < roll < 60:
        froll = 7
    if 59 < roll < 75:
        froll = 8
    if 74 < roll < 100:
        froll = 4
    cards (player, player2, froll)
    # the game ends if the enemy is no longer flying
    if flight(player) > 0:
        game_over=True
    return 0

def cards(player, player2, choice):
    #this function represents the choices that can be made by the players, this function is in charge of calling each card's function.
    if (choice == 1):
        show_stats(player2)
    if (choice == 2):
        guns_on(player,player2)
    if (choice == 3):
        climb(player)
    if (choice == 4):
        descend(player)
    if (choice == 5):
        immelman(player)
    if (choice == 6):
        split_s(player)
    if (choice == 7):
        level_off(player)
    if (choice == 8):
        disengage(player,player2)
    return 0

def print_options(H,V,L):
    # prints options for human players
    print("\nAltitude:", H, "m" ,"\nAirspeed:", V ,"kph", "\nAmmo count:", L, "\n" )
    print("Select a Maneuver:" )
    print("     1: Reveal Enemy Stats")
    print("     2: GUNS ON!")
    print("     3: Climb")
    print("     4: Descend")
    print("     5: Immelman Turn")
    print("     6: Split S")
    print("     7: Level Off")
    print("     8: Disengage")
    print("     9: Quit\n")
    return 0

def flight(player):
    # under the certain conditions, the plane can no longer continue to fly.
    if player.h < 200:
        print(" \n",player.name, "crashed\n")
        return 1
    if player.v < 200:
        print(" \n",player.name, "stalled\n")
        return 1
    if player.l < 0:
        print(" \n",player.name, "is out of Ammo\n")
        return 1
    if player.v > 1.3*player.s:
        print(" \n",player.name, "exceeded max airspeed\n")
        return 1
    else:
        return 0

def show_stats(player):
    #reveals the stats of the enemy player
    print("\n\nEnemy Stats:","\nAlt:", player.h, "m\nSpd:", player.v, "kph\n\n")
    return 0

def guns_on(player, player2):
    global game_over
    global hard_mode
    # if a player is within 150 meters of their opponent, they are allowed to open fire
    print(player.name, "attempted to move to guns-on position\n")
    if -150<player.h-player2.h<150:
        print(player.name, "took a shot\n")
        time.sleep(1.5)
        # uses an ammo consumption multiplier and a randomized integer to determine how much ammo is spent
        player.l= player.l - (player.m)*(random.randint(40,200))
        if (hard_mode == True):
            # the game rolls a virtual die to see if a hit is scored
            if random.randint(1,7) > 6:
                print(player.name, "won.")
                game_over=True
                outro()
            else:
                print(player.name, "missed\n")
        else:
            # in hard mode, the chances of landing a shot are reduced
            if random.randint(1,10) > 6:
                print(player.name, "won.")
                game_over=True
                outro()
            else:
                print(player.name, "missed\n")
    else:
        time.sleep(0.5)
        print(player.name, "can't get a clear shot")
    return 0

def climb(player):
    # the player climbs for 30 seconds, hence their new altitude is determined by their climb rate
    player.h = player.h + 30*(player.c)
    # climbing comes with a marginal loss of speed
    player.v = 0.95*player.v
    print(player.name, end="")
    print(" started climbing...\n")
    return 0

def immelman(player):
    # the player climbs more agressively, yet loses a significant proportion of their speed
    player.h = player.h + 60*player.c
    player.v = player.v - (70+0.1*player.v)
    print(player.name, end="")
    print(" pulled an Immelman!!\n")
    return 0

def split_s(player):
    # the opposide of an immelman, but the descent is not as agressive, accompanied by an increase in speed.
    player.h = player.h - 40*player.c
    player.v = player.v + (70+0.15*player.v)
    print(player.name, end="")
    print(" pulled a Split-S!\n")
    return 0

def level_off(player):
    # as the speed of a player increases, this logarithmic function makes sure that this card's effects don't compound. As this card is played at high speeds, it becomes less effective
    player.v = 80*(player.v**0.3+(1/player.v))
    print(player.name, end="")
    print(" leveled off!\n")
    return 0

def disengage(player,player2):
    global game_over
    # if a player's speed is more 100 kph greater than your opponent, they can disengage. If the speed difference is insufficient, they'll fail to break away.
    if (player.v > 100 + player2.v):
        time.sleep(2)
        print(player.name, end="")
        print (" successfilly disengaged")
        game_over=True
        outro()
    else:
        time.sleep(2)
        print(player.name, end="")
        print(" failed to break away")
    return 0

def descend(player):
    # this card represents a fixed descent of 150m, creating opportunities for finer levels of control.
    player.v = player.v + 50
    player.h = player.h - 150
    print(player.name,"started descending...\n")
    return 0

def loading_screen():
    #prints a dot, when compounded in a loop, this can create a loading bar.
    print(". ", end="")
    time.sleep(0.2)
    return 0

def tutorial():
    print("\n\n\nHello, welcome to TBCB Dogfighters\n")
    time.sleep(2)
    print("\nLet's start with your flight training.")
    time.sleep(4)
    print("\nYou will be pitted against foes of ranging competence and ability. To stand a chance of survival, you need the tools to fend them off")
    time.sleep(6)
    print("\nYou can play a grand total of 8 cards, when played correctly, you'll be unstopabble")
    time.sleep(6)
    print("\n1: Reveal Enemy Stats")
    print("This card reveals the approximated speed and altitude of your foe, using it too often will waste precious time.")
    time.sleep(6)
    print("\n2: GUNS ON!")
    print("This card is your highway to a checkmate. Be careful as not to waste your ammo, as each shot will cost you. To use this card, you must be close to your enemy in both alt. and speed.")
    time.sleep(6)
    print("\n3: Climb")
    print("This card will increase you alt., with a slight decrease in speed.")
    time.sleep(5)
    print("\n4: Descend")
    print("This card will decrease you alt., with a slight increase in speed.")
    time.sleep(7)
    print("\n5: Immelman Turn")
    print("This card will give you a massive increase in alt., but with an equally giant decrease in speed. If you drop below 200 kph, you'll stall and lose the game")
    time.sleep(6)
    print("\n6: Split S")
    print("This card is the exact opposite of the Immelman, be careful using it near the ground")
    time.sleep(6)
    print("\n7: Level Off")
    print("This card gives you a marginal increase in speed, holding altitude constant")
    time.sleep(6)
    print("\n8: Disengage")
    print("This card gives you a second endgame option, to disengage you must be sufficiently faster than your foe")
    time.sleep(6)
    print("\n9: Quit\n")
    print("Exits the game.")
    return 0

def intro():
    print("\nUntitled.com Productions Ltd. Inc. Corp. \n")
    time.sleep(2)
    print("Presents...\n")
    time.sleep(2)
    print("TBCB Dogfighters\n")
    time.sleep(3)
    print("\n[Spechalske Approved]\n")
    time.sleep(2)
    return 0

def choose_plane():
    # promts for user imput, repromts when the choice in invalid. If the choice is succesful, the player is assigned a plane.
    while True:
        try:
            plane=int(input("\nChoose your plane:\n    1. P-47D-25\n    2. P-51D-5\n    3. Spitfire F Mk. IX\n    4. La-7\n    5. View stats\nChoice (please input a number):"))
            if plane ==1:
                player = P47()
            if plane ==2:
                player = P51()
            if plane ==3:
                player = Spitfire()
            if plane ==4:
                player = La7()
            if plane ==5:
                # if a player wishes to view the stats, the statcards are printed and the choice selection process starts over.
                print_stats()
                time.sleep(1)
                player = choose_plane()
        except ValueError:
            print("\nPlease choose an option by typing a number between 1 and 5.")
            continue
        if plane > 5 or plane < 1:
            print("\nPlease choose an option by typing a number between 1 and 5.")
            continue
        else:
            break
    return player

def choose_mode():
     # promts for user imput, repromts when the choice in invalid. If the choice is succesful, the game is set to a specific mode
    while True:
        try:
            mode = int(input("\nSelect a difficulty:\n    1.Easy    -- (Shows rough enemy location)\n    2.Normal  -- (standard gameplay, knowing climb rates is essential)\n    3.Hard    -- (Decreased odds of landing a shot)\nChoice (please input a number):"))
        except ValueError:
            print("\nPlease choose an option by typing 1, 2, or 3.")
            continue
        if mode > 3 or mode < 1:
            print("\nPlease choose an option by typing 1, 2, or 3.")
            continue
        else:
            break
    return mode

def tutorial_choice():
    # promts for user imput, repromts when the choice in invalid. If the choice is succesful, the game plays or skips the tutorial
    while True:
        try:
            tut = int(input("\nWould you like to skip the tutorial?\n    1. Yes\n    2. No\nChoice (please input a number):"))
        except ValueError:
            print("\nPlease choose an option by typing 1 or 2.")
            continue
        if tut > 2 or tut < 1:
            print("\nPlease choose an option by typing 1 or 2.")
            continue
        else:
            break
    return tut

def pvp():
    # promts for user imput, repromts when the choice in invalid. If the choice is succesful, the game is set to either single player or pvp mode
    global pvp_mode
    while True:
        try:
            pvp = int(input("\nSelect a mode\n    1. Single Player\n    2. 2 player PvP\nChoice (please input a number):"))
        except ValueError:
            print("\nPlease choose an option by typing 1 or 2.")
            continue
        if pvp > 2 or pvp < 1:
            print("\nPlease choose an option by typing 1 or 2.")
            continue
        else:
            break
    if pvp == 1:
        pvp_mode=False
    else:
        pvp_mode=True

def print_stats():
    print("\nP-47:\n     Climb rate: 11 m/s\n     Top Speed: 700 kph\n     Ammo Count: 3400 rounds\n")
    time.sleep(3)
    print("\nP-51:\n     Climb rate: 18 m/s\n     Top Speed: 698 kph\n     Ammo Count: 2080 rounds\n")
    time.sleep(3)
    print("\nSpitfire:\n     Climb rate: 20 m/s\n     Top Speed: 650 kph\n     Ammo Count: 1640 rounds\n")
    time.sleep(3)
    print("\nLa-7:\n     Climb rate: 18 m/s\n     Top Speed: 670 kph\n     Ammo Count: 340 rounds\n")

def outro():
    global game_over
    if game_over == True:
        print("\nGAME OVER\n")
        print("Thank you for playing!!")
if __name__ == "__main__":
    main()

