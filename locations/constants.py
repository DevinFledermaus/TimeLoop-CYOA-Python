import random
from os import system, name

# Classes
# Protagonist
class Mafia:
    strength = 4
    speed = 4
    intelligence = 3
    luck = 3
    intimadation = 3
    social = 3
    time_left = 24
    repeats = 0
    archetype = "Mafia"
    apt_clue = False
    rooftop_clue = False
    
class Military:
    strength = 5
    speed = 5
    intelligence = 4
    luck = 3
    intimadation = 3
    social = 3
    time_left = 24
    repeats = 0
    archetype = "Ex-Military"
    apt_clue = False
    rooftop_clue = False
    
class Lawyer:
    strength = 3
    speed = 3
    intelligence = 6
    luck = 3
    intimadation = 3
    social = 3
    time_left = 24
    repeats = 2000
    archetype = "Lawyer"
    apt_clue = False
    rooftop_clue = False
    
    
# # Mercenaries
# class Merc1:
#     health = 10
#     strength = 5
#     speed = 5
#     intelligence = 5
#     tracking = 5
#     name = "Merc 1"
    
# class Merc2:
#     health = 10
#     strength = 5
#     speed = 5
#     intelligence = 5
#     name = "Merc 3"
    
# class Merc3:
#     health = 10
#     strength = 5
#     speed = 5
#     intelligence = 5
#     name = "Merc 3"
    
    ##############

# Functions
# Character Select        
def charSelect():
    clear()
    print("Select your character!")
    selection = input("1. Mafia \n2. Ex-Military \n3. Lawyer \n")
    if selection == '1':
        character = Mafia
        clear()
        print("You have selected the ", character.archetype)
        print("You possess")
        print(character.strength, "strength")
        print(character.speed, "speed")
        print(character.intelligence, "intelligence")
        print(character.luck, "luck")
        print(character.intimadation, "intimadation")
        print(character.social, "social")
        return character
    elif selection == '2':
        character = Military
        clear()
        print("You have selected the ", character.archetype)
        print("You possess")
        print(character.strength, "strength")
        print(character.speed, "speed")
        print(character.intelligence, "intelligence")
        print(character.luck, "luck")
        print(character.intimadation, "intimadation")
        print(character.social, "social")
        return character
    elif selection == '3':
        character = Lawyer
        clear()
        print("You have selected the ", character.archetype)
        print("You possess")
        print(character.strength, "strength")
        print(character.speed, "speed")
        print(character.intelligence, "intelligence")
        print(character.luck, "luck")
        print(character.intimadation, "intimadation")
        print(character.social, "social")
        return character
    else:
        print("Invalid Input")
        charSelect()

        
# # Enemy Select
# def enemySelect(Merc1, Merc2, Merc3):
#     enemyList = [Merc1, Merc2, Merc3]
#     chance = random.randint(0,2)
#     enemy = enemyList[chance]
#     if enemy.health > 0:
#         return enemy
#     else:
#         enemySelect(Merc1, Merc2, Merc2)
        
# Next
def next():
    print("")
    input("Press Enter to Continue...\n")
    # windows name (nt)
    # linux and mac name (posix)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    stats(character)
        
# Clear
def clear():
    # windows name (nt)
    # linux and mac name (posix)
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
        
        
# Display Stats
def stats(character):
    if character.repeats == 0:
        pass
    else:
        if character.time_left < 2:
            print("Hours Left before Loop: <1    -    Repeats: ", character.repeats)
            print("")
            print("")
        else:
            print("Hours Left before Loop: ", character.time_left, "    -    Repeats: ", character.repeats)
            print("")
            print("")
    
def tick(character):
    character.time_left = character.time_left - 1
    
# End Current Loop
def endLoop(character): # to loop add function into a while loop that states time left greater than zero
    character.time_left = 0
    
def reset(character):
    if character == Mafia:
        character.strength = 4
        character.speed = 4
        character.intelligence = 3
        character.luck = 3
        character.intimadation = 3
        character.social = 3
        character.time_left = 24
    elif character == Lawyer:
        character.strength = 3
        character.speed = 3
        character.intelligence = 6
        character.luck = 3
        character.intimadation = 3
        character.social = 3
        character.time_left = 24
    else:
        character.strength = 5
        character.speed = 5
        character.intelligence = 4
        character.luck = 3
        character.intimadation = 3
        character.social = 3
        character.time_left = 24
    
# Adjust Loop stats (increases repeat and starts loop)
def loop(character):
    character.repeats = character.repeats + 1
    reset(character)


# # Random Encounters
# def encounter():
#     pass
    
    
character = charSelect()
# enemy = enemySelect(Merc1, Merc2, Merc3)