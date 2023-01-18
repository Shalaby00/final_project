# final_project
(don't play hard mode)


In the README file for your project, use Markdown to include all of the following information:
* A video of your program running (1min or less, no voiceover)


* Summarize program's functionality (what does it do?) and purpose (why does it exist and/or who is it for?):

Hello. TBCB Dogfighters is a turn based, card based, WWII dogfighting simulator. In this game, you can play against a computer controlled opponent or another player. Your goal is to use a selection of cards to successfully down your opponent. There are three potential endgame scenarios. You can win by shooting down your foe, you can draw by disengaging, and you can lose if your foe successfully shoots you down.

The purpose of this game is giving me an opportunity to explore class-object oriented programming. Additionally, I wanted to challenge myself with the task of creating a competitive digital opponnent. Although this product has no practical use, it serves as a good sandbox for experimenting with my cs knowledge so far, allowing me to embark on my own path of discovery.

* A description, with code segments, of a "breakthrough moment" in which you solved a particularly difficult problem, learned to do something new, or independently overcame being stuck

Let's take the following example:
```class Foe():
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
Now, I can pass these values through one of my cards:

```
    def level_off(player):
        player.v = 80*(player.v**0.3+(1/player.v))
        print(player.name, end="")
        print(" leveled off!\n")
        return 0
```
    
As the speed of a player increases, this logarithmic function makes sure that this card's effects don't compound. As this card is played at high speeds, it becomes less effective.

* An explanation of data abstraction as it is used in your program.




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
- Include code segments that show where data is being stored and where data is being retrived and accompanying explanation.
- Identify what the abstracted data represents in your program
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

