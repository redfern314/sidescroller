"""
PoeGameMechanical
All measurements in inches, inches/second
"""

class World():

    """
    MechWorld Constructor
    """
    def __init___(self, start_speed):
        self.direction = True #True is forward
        self.speed = start_speed
        self.maxSpeed = 100
        self.grid = None

    """
    Sets the speed at which the world is moving,
    in inches per second
    """
    def setSpeed(self, newSpeed):
        if newSpeed < self.maxSpeed:
            self.speed = newSpeed


class Snail():

    """
    Constructor for a mechanical implementation of the
    snail. 
    """
    def __init__(self, start_location, x_location):
        Snail.__init__(self)
        self.location = start_location
        self.xshift = x_location
        self.velocity = 0 #in px per frame
        self.fallRate = .25 #in px per frame^2
        self.liftRate = -.5 #in px per frame^2
        self.isLift = False

    """
    Gets the snail's locatioin relative to the vision grid
    """
    def getGridLocation(self):
        return (self.xshift, self.location)

    """
    Checks if the snail is being lifted, and moves it accordingly
    """
    def move(self):
        if self.isLift:
            self.velocity += self.liftRate
        self.velocity += self.fallRate
        self.location += self.velocity


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


