from .constants import Lawyer, Mafia, Military, endLoop, next, character, tick
from .hallway import hallway

def apt(character):
    next()
    print("You start awake in bed again.")
    print("")
    if character == Lawyer:
        if character.repeats == 2000:
            rep1()
        elif character.repeats == 2001:
            rep2()
    else:
        if character.repeats == 0:
            rep1()
        elif character.repeats >= 1:
            rep2()
        
        
def rep1():
    next()
    
    if character == Lawyer:
        pass
    
    else:
        print("Your head feels heavy with a hangover caused by last nights partying.\nYou remember going to a party for your twin brother's welcome home.")
        print("Although you call it a welcome 'party', it was just you and your brother.")
        
        if character == Mafia:
            print("The income of military personel isn't that great so you decided to spoil your brother a bit.")
            print("You went all out, using your connections got into the most exclusive club.")
            print("And for the rest of the weekend. You got a penthouse at the top hotel in the city.")
            next()
        else:
            print("Your brother is quite well off so he never lets you pay for anything when you're together and blames it on 'you protect our country, the least I can do pay for lunch', or something of the sort.")
            print("He mentioned going out for the night and living like royalty for the weekend.")
            next()
        
        print("Sitting on your bed you laugh to yourself and while you hold your head you promise never to drink that much again.")
        print("You recall the party quite well actually, you remember you and your brother stumbling into the back of a cab, headed home, but that's where it ends.")
        print("You don't remember getting to the hotel, you don't remember entering the elevator, you don't remember reaching the penthouse and you definetly don't remember getting undressed and climbing into bed.")
        print("The sound of the alarm clock pulls your from your thoughts and you banish the thoughts.")
        tick(character)
        next()
        print("The call of nature is what prompts you to climb out of bed and head to the bathroom")
        print("Inside you take the oppurtunity to freshen up and shower your hangover away.")
        print("Once you finish up in the bathroom you head to the kitchen, walking past the clock you note the time just as it hits 09h00, just as the coffee machine beeps.\nYou head over to grab yourself a cup.")
        print("After you enjoy a cup of coffee you decide to get ready, you have a couple hours to kill before you have to be somewhere else.")
        next()
        
        if character == Mafia:
            print("You dont have much time as you got a job to do before you can come back and spend the rest of the weekend with your brother.")
            print("As such, you won't have much time to go home and get your equipment. You'll have to make do with what you got on hand.")
            print("Your delievery arrived as plan.")
            print("As a capo, you have quite a few hands at your beck and call, and an associate delievered your 'over-night' bag, along with your custom suit.")
            next()
            print("You take everything out the bag and place it all on the bed, one by one.")
            print("First your trusted custom 1911 handgun, suppressor along with it.\nJust a couple extra magazines of ammo.")
            print("A lockpick set.")
            print("An alias, in the form of a fake id and driver's license, in case you need a change of identity.")
            print("And of course your signature weapon, A hunting knife with a custom handle shaped into brass knuckles.\nUseful incase you feeling like cutting and stabbing or bashing a skull in.")
            next()
            print("Your suits have also been altered. Each suit, comes with an inner layer made of a dense, lightweight mesh.")
            print("Just enough to match a kevlar vest, yet you look better. It also has a few hidden pocket allowing you to hid a few surprises in there.")
            tick(character)
            print("Satisfied you dress and conceal all your things.")
            next()
            print("Dressed, you quickly check your phones, checking for updates on the target.")
            print("There's another reason you chose this hotel in particular.")
            print("Apart from being a leader of a whole branch of the family, you also their greatest hitman.")
            print("You always called when there's a thorn in the family that needs to be remove with effectively and permantly.")
            next()
    
        else:
            print("Mili")
            
        print("You leave your suite and head to your brother's to check on him before heading out.")
        print("Knocking on the door you check the time on your watch.")
        print("10H46")
        print("It'll take about 10 mins to drive to there so you can't really waste anymore time here.")
        print("As you turn to leave, you feel it in the floor before anything else.")
        print("A loud explosion and violent tremors ripple throughout the building.")
        print("You get thrown around and knocked unconscious.")
        tick(character)
        tick(character)
        tick(character)
        tick(character)
        tick(character)
        tick(character)
        tick(character)
        next()
        print("You wake up in a hospital room and a nurse tending to you.")
        print("As a detective walks in the nurse quickly turns and leaves.")
        print("The detective questions you for a long time")
        endLoop(character)
    
    #########
    
def rep2():
    next()
    print("2nd time in the apartment")
    hallway()