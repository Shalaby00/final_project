# final_project
(don't play hard mode)

[acm.webm](https://user-images.githubusercontent.com/106011563/213141804-0eff0eac-8eb2-4ab4-b7fd-535b27a9adc7.webm)

* Program Summary:

Hello. TBCB Dogfighters is a turn based, card based, WWII dogfighting simulator. In this game, you can play against a computer controlled opponent or another player. Your goal is to use a selection of cards to successfully down your opponent. There are three potential endgame scenarios. You can win by shooting down your foe, you can draw by disengaging, and you can lose if your foe successfully shoots you down.

The purpose of this game is giving me an opportunity to explore class-object oriented programming. Additionally, I wanted to challenge myself with the task of creating a competitive digital opponnent. Although this product has no practical use, it serves as a good sandbox for experimenting with my cs knowledge so far, allowing me to embark on my own path of discovery.

* "Breakthrough Moment"

The largest turning point in my process revolved around adopting a class-object system to facilitate gameplay. I established each plane as it's own object, allowing me to store data belonging to each plane in an efficient manner. Using this system, I can minimize the amount of information I have to pass between different functions. 

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

This system allowed me to overcome significant challenges when it came to introducing plane selections and pvp mode. Ultimately, it enabled me to use the same 'cards' for all of my players, regardless of their aricraft. Both human and computer opponents now share the same set of move functions, drastically simplifying my code. 


* An explanation of data abstraction as it is used in your program.

Although I have touched on the class-object system I've used, I'll elaborate further on how this system is used for the purpose of data abstraction.

Below is an example of this system at use. This function is used to select an aircraft. When the selection is made, the player is assigned to a plane (under this system, each plane is an object):

```
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
```
This function crucially displays the retrieval of data by allocating objects to the player when called upon. Each object contains variables that keep track of the plane's climb rate, top speed, airspeed, altitude, and ammo reserves. The objects enable me to store the data for later use, without having to redifine each variable for every function.

- Include code segments that show where data is being stored and where data is being retrived and accompanying explanation.


- Explain how the selected abstraction manages complexity in your program code (why your program code could not be written, or how it would be written differently, if you did not abstract the data in the way you did)

* An explanation of procedural abstraction as it is used in your program.

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

- Include a single code segment containing:
* A procedure
- with a parameter (i.e., takes an argument)
* and includes an algorithm
- that uses sequencing, selection, and iteration
* and returns a value
- that depends on the arguments given when the procedure is called
* and is called from elsewhere in the program
- Explain how the algorithm in the above code segment functions and why it is important for the purpose of your program
- Explain how the procedural abstraction helps to manage complexity in your program (be specific!)

