""""
@Chloe Vilain
@4/11/2013
@V 1.3

This file contains the baseline architecture of the game.
All classes should be considered 'abstract' parent classes to
GameGraphics.py and GameMechanical.py
Included class definitions:
World-- The world in which the game functions
Snail-- The player-controlled character in the game
Modifier-- Bonuses and Poisons the player character encounters
VisionAdaptor-- Interface with the vision component of the project.
"""

import time
import random


"""
A representation of the World for the game
Designed to serve as an abstract parent class for
graphic and mechanical implementations
"""
class World(object):

    default_gravity = 1
    default_speed = 100
    default_direction = 1
    default_point_rate = 1
    
    '''
    Constructor for World
    Sets the world's default location, the speed of the
    game, the strength of gravity, and the direction of motion
    '''
    def __init__(self):
        self.location = 0
        self.gravity = World.default_gravity
        self.speed = World.default_speed
        self.direction = World.default_direction
        self.points = 0
        self.pointsRate = World.default_point_rate

    def __string__(self):
        return "World object"

    """
    sets the speed to a given new speed
    Note that lower number indicates faster
    If speed reaches upper bound, sets it to max speed
    """
    def setSpeed(self, new_speed):
        if new_speed<30:
            new_speed = 30
        else:
            self.speed = new_speed


    def setGravity(self, new_gravity):
        self.gravity = new_gravity

    """
    Reverses direction of movement
    """
    def invertDirection(self):
        self.direction = -1*self.direction

    
"""
A representation of the Snail for the game
Designed to serve as an abstract parent class for
graphic and mechanical implementations
"""
class Snail(object):

    default_location = (300,300)
    default_fallRate = 10
    default_liftRate = 30


    """
    Constructor for Snail
    Sets the location (tuple), fallrate(integer, and liftRate(integer) to their
    relative default values
    """
    def __init__(self):
        self.location = Snail.default_location
        self.fallRate = Snail.default_fallRate
        self.liftRate = Snail.default_liftRate

    def __string__(self):
        return "Snail Object"

    """
    Sets the fall rate to a given integer
    If slower than 0, sets to 1
    """
    def setFallRate(self, newFallRate):
        if newFallRate<1:
            self.fallRate = 1
        else:
            self.fallRate = newFallRate

    '''
    Adjusts the snail's location on fall.
    '''
    def fall(self):
        self.location = (self.location[0],self.location[1]+self.fallRate)

    '''
    Moves the snail to the given location (tuple)
    '''
    def setLocation(self, newLocation):
        self.location = newLocation

    def onEventLift(self, lift = -30):
        self.location = (self.location[0], self.location[1]+lift)
        
"""
A representation of the Modifier for the game
Designed to serve as an abstract parent class for
graphic and mechanical implementations
"""    
class Modifier(object):
    

    '''
    Constructor for a Modifier object
    takes a string for the type (either poison or bonus)
    and the modifier's location in the world.
    '''
    def __init__(self, location, typeEffect = None):
        #self.mod_type = self.chooseType()
        #self.chooseEffect()
        #self.type = typeEffect
        self.type = self.chooseType()
        self.location = location

    def __string__(self):
        return self

    def chooseType(self):
        if random.random()<.5:
            return 'poison'
        return 'bonus'

    
    bonuses = ['point_bonus', 'point_rate']
    poisons = ['point_deduction', 'point_rate_poison']

            
            
    '''
    Sets the effect, bonus or poison
    Passes it to setBonus or setPoison to implement
    '''
    def chooseEffect(self):
        if self.type == "poison":
            self.setPoison(Modifier.poisons[random.randint(0,len(Modifier.poisons)-1)])
        elif self.type == "bonus" :
            self.setBonus(Modifier.bonuses[random.randint(0, len(Modifier.bonuses)-1)])

    """
    location setter
    """
    def setLocation(self, location_new):
        self.location = location_new

    def setType(self, effectType):
        self.type = effectType
        
 
    '''
    Chooses a poison effect from the list or poisons
    '''
    def setPoison(self, effect):
        #why oh why u no switch case
        if effect == "point_deduction":
            print world.points
            world.points+=-50
            print world.points
        elif effect == 'point_rate_poison':
            world.pointRate+=-.5
            self.poisonTimer = 0
        elif effect == 2:
            #do stuff
            pass
        elif effect == 3:
            #do stuff
            pass

    '''
    Chooses a bonus effect from the list of bonuses
    '''
    def setBonus(self, effect):
        if effect == 'point_bonus':
            world.points+=50
        elif effect == 'point_rate':
            world.pointRate+=.5
            self.bonusTimer = 0
        elif effect == 2:
            #do stuff
            pass
        elif effect == 3:
            #do stuff
            pass

    """
    Activates the effect designated by the object
    """
    def activateEffect(self):
        #activates the effect
        return

    """
    Resets the modifier to a new random selection.
    NOTE only pertinant to Mech Implementaion
    """
    def onActivationReset(self):
        this.chooseEffect()

"""
Vision adaptor to interface between the vision component and
the game engine
"""
class VisionAdaptor(object):

    def __init__(self):
        pass

    def __string__(self):
        return self

"""
Test Code
"""
def main():
    myWorld = World()
    mySnail = Snail()
    myPosion = Modifier("poison",(1,1))

main()


