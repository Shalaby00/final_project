# final_project
(don't play hard mode, it's too hard)

[acm.webm](https://user-images.githubusercontent.com/106011563/213141804-0eff0eac-8eb2-4ab4-b7fd-535b27a9adc7.webm)

## Program Summary:

TBCB Dogfighters is a turn based, card based, WWII dogfighting simulator. In this game, you can play against a computer controlled opponent or another player. Your goal is to use a selection of cards to successfully down your opponent. There are three potential endgame scenarios. You can win by shooting down your foe, you can draw by disengaging, and you can lose if your foe successfully shoots you down.
The purpose of this game is giving me an opportunity to explore class-object oriented programming. Additionally, I wanted to challenge myself with the task of creating a competitive digital opponent. Although this product has no practical use, it serves as a good sandbox for experimenting with my CS knowledge so far, allowing me to embark on my own path of discovery.

## "Breakthrough Moment"
The largest turning point in my process revolved around adopting a class-object system to facilitate gameplay. I established each plane as its own object, allowing me to store data belonging to each plane in an efficient manner. Using this system, I can minimize the amount of information I have to pass between different functions.
Let's take the following example:
```
class Foe():
    def __init__(self):

        self.name= 'FW-190'
        self.s=700
        self.c=15
        self.a=500
        self.m=1

        self.l= self.a
        self.h=1200
        self.v=400
```

After I've assigned this object to a player, I can pass the values stored within the object through one of my functions:
```

def climb(player):
    # the player climbs for 30 seconds, hence their new altitude is determined by their climb rate
    player.h = player.h + 30*(player.c)
    # climbing comes with a marginal loss of speed
    player.v = 0.95*player.v
    print(player.name, end="")
    print(" started climbing...\n")
    return 0
```

Instead of taking an argument for each variable, I simply have to pass the function an object. Hence, I can manipulate the data stored within each object without having to resort to verbose and convoluted code for modifying each plane's parameters.
This system allowed me to overcome significant challenges when it came to introducing plane selections and pvp mode. Ultimately, it enabled me to use the same 'cards' for all of my players, regardless of their aircraft. Both human and computer opponents now share the same set of move functions, drastically simplifying my code.

## Data Abstraction
Although I have touched on the class-object system I've used, I'll elaborate further on how this system is used for the purpose of data abstraction.
Below is an example of this system at use. This function is used to select an aircraft. When the selection is made, the player is assigned to a plane (under this system, each plane is an object):

```
def choose_plane():
    # prompts for user input, reprints when the choice in invalid. If the choice is successful, the player is assigned a plane.
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
                # If a player wishes to view the stats, the stat cards are printed and the choice selection process starts over.
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
```

This function crucially displays the retrieval of data by allocating objects to the player when called upon. Each object contains variables that keep track of the plane's climb rate, top speed, airspeed, altitude, and ammo reserves. The storage of the data is facilitated by classes, such as the following:

```
class P51():
    def __init__(self):
        self.name= 'You'
        self.s=698
        # ^ the top speed
        self.c=18
        # ^ the climb rate
        self.a=2080
        # ^ the # of initial ammo
        self.m=2
        # ^ ammo spending multiplier

        self.l= self.a
        # ^ ammo left
        self.h=1800
        # ^ starting alt. (active)
        self.v=400
        # ^ spawning speed (active)
```

The object enables me to store the data for later use, without having to redefine each variable for every function, ultimately reducing the complexity of my code. In the absence of such a system, it would be incredibly difficult to use the same 'card' functions for both the player and their opponent.

## Procedural Abstraction

This is an example of procedural abstraction. This function hosts numerous algorithms, revolving around sequencing and selection. This function takes two arguments (i.e. , the two player objects), allowing me to manipulate the data belonging to each of these objects. This function contains conditional statements that form the building blocks of my selection-oriented algorithms. For example, the ability of a player to take a shot is dependent on the difference in altitude between them and their foe, hence I use boolean expressions and an else-if sequence to determine if a shot is possible. Moreover, the likelihood of landing a shot is dependent on whether hard mode is engaged. In order to do this I use a global variable to represent whether hard mode is engaged or not. Then I use some conditional statements to alter the likelihood of making a shot based on the game mode.

```
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
```

However, because this function results in a direct change to the course of the game I didn't feel the need to return anything. However, in another function I return a value to the main function. For example:

```
def tutorial_choice():
    # prompts for user input, reprints when the choice in invalid. If the choice is successful, the game plays or skips the tutorial
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
```

This function uses an iterative algorithm to prompt the user for input when the user inputs invalid values. Once the user makes an acceptable choice, that value is returned to the main function, and is used as such:

```
def main():
    # Each global variable represents a game setting that can be tripped by any function, affecting the entirety of the game.
    global game_over
    global easy_mode
    global hard_mode
    global pvp_mode
    intro()
    # This code enables choosing tutorial settings, pvp modes, and game mode.
    tut= tutorial_choice()
    if (tut == 2):
        tutorial()
    pvp()
    
    ...
    etc.
    ...
```


This function is called when the time comes for the user to choose whether or not to do the tutorial, making sure that the user picks a valid course of action.

Overall, procedural abstraction drastically simplifies my code. Since my game is card based, I can represent each card as a specific function (similar to the '`GUNs ON!!" card shown above). Moreover, when running my main function, I've chosen to abstract each phase of my introduction, including the mode choices that the player has to make.
