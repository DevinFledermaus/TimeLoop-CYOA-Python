from .apartment import apt
from .constants import Lawyer, Mafia, reset, next, character, loop

def prologue(character):
    next()
    ##########
    print("This is the prologue")
        
def flow(character):
    while character.time_left > 0:
        apt(character)
    else:
        loop(character)
        apt(character)
    

def start():
    prologue(character)
    flow(character)