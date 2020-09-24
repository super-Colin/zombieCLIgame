
import random

def confirmAction(msg):
    print(msg)
    feedBack = input('"n" to cancel or enter to continue')
    if feedBack == 'n' or feedBack == 'N':
        return False
    else:
        return True


class World:
    def __init__(self):
        self.dayNight = "day"
        self.timeLeft = 12
        self.dayNumber = 1
        self.difficulty = 1 # Will ramp up very slowy over time, 1.02..
        self.tasks = {
            "rest": ["Helps you heal, recovers energy", 2], # "taskName:": ['description', timeTaken]
            "build": ["Use materials to improve your base", 3],
            "scout": ["Scouting increases your chances of finding nice things", 2],
            "loot": ["Leave the base and search for useful things", 4]
        }


    def getTimeLeft(self):
        return self.timeLeft
    def getDayNight(self):
        return self.dayNight
    def getDayNumber(self):
        return self.dayNumber
    def getTasks(self):
        return list(self.tasks.keys()) # only return the task names
    def getTaskInfo(self, choice):
        if choice in self.tasks:
            return self.tasks[choice]
        else:
            return 'No such task'


    def isThereAnAttack(self): # Roll to see if there is an attack 
        if self.dayNight == 'day': # An attack is less likely by zombies 
            return 0
        else:
            return 1


    def createAttack(self): # Create an amount of damage for an ambush in the night (or day)
        ambientDamage = round(self.dayNumber / 7)
        attackStrength = random.randrange(ambientDamage, ((10 * self.difficulty) + ambientDamage))
        return round(attackStrength)


    def changeDayNight(self): # Just progress the day to night, night to the next day
        if self.dayNight == "day":
            self.dayNight = "night"
            return 'Night sets upon you '
        else:
            self.dayNight = "day"
            self.dayNumber += 1 # if it's a new day add increment dayNumber
            self.difficulty += 0.02 # the world hates you
            return 'It is now day, number ' + self.dayNumber


    def useTime(self, timeTaken): # Check something doesn't take more time than you have, or progress dayNight if needed
        if timeTaken > self.timeLeft:
            return self.changeDayNight() 
        else:
            self.timeLeft -= timeTaken
            return self.timeLeft

    def performTask(self, choice):
        # https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
        if choice == 'scout':
            foundSomething = round(random.randrange(0, 100) / 100) # Make a decimal number between 0 ~ 1 and round it to be used as a boolean
            if foundSomething:
                return 'you found something'
            else:
                return 'you found nothing'

        elif choice == 'nothing':
            return 'nothing'

        
 


class Base():
    def __init__(self):
        self.health = 100
        self.barricade = 20
        self.defenseLevel = 0
        self.defenseMultiplier = 1
        self.craftLevel = 0
        self.toolLevel = 0
        self.storage = []
        self.luck = 1

    def getBase(self):
        baseString = ( '' )

    def repairBarricade(self, mulitplier):
        barricadeToAdd = round(random.randrange(8, 15) * mulitplier) + self.toolLevel
        self.barricade += barricadeToAdd


    def attackOnBase(self, attack):
        damageDone = round(attack - (self.defenseLevel * self.defenseMultiplier)) - self.defenseLevel
        self.barricade -= damageDone



class Player:
    def __init__(self):
        self.name = 'Jim'
        self.health = 100
        self.water = 100
        self.food = 100
        self.energy = 100
        self.status = "Healthy & Happy"
        self.workMultiplier = 1
        self.inventoryMax = 8
        self.inventory = []
        self.tasks = {
            
        }

    def getStatus(self):
        statusString = (self.name + ' the person,\nHealth = ' + str(self.health) + ',\nWater = ' + str(self.water) + ',\nFood = ' + str(self.food) + ',\nEnergy = ' + str(self.energy) + ',\nStatus = ' + str(self.status) + '\nInventory = ' + str(self.inventory) )
        return statusString
    
    # def dontLetOver100(self, stat):
    #     if self[stat] > 100:
    #         self[stat] = 100

    def setName(self, name):
        self.name = name
    
    def rest(self):
        self.health += 10
        self.energy += 15

    def eat(self):
        self.food += 20
        self.water += 10
        self.energy += 5

    def drink(self):
        self.water += 20



# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------

world = World()
base = Base()
player = Player()


# print('Welcome to Zombie Survival Game')
# player.name = input('Player Name: ')
# print(player.name)

# print('There are zombies and shit outside so making trips outside is always risky')
# print('You can always use "help" to find out more')

# print("During the day it's safer to stay inside and work on your base")
# print("During the night it's easier so sneak to locations for supplies, but your base is more likely to be attacked")

# print('You find yourself in an abandoned old house.')


while base.health > 0:

    print('\nIt is currently ' + world.getDayNight() + ' on day# ' + str(world.getDayNumber()) )
    choice = input( "What would you like to do? (\"help\" if you're lost, \"end\" to quit)\n")

    if choice in world.getTasks():
        info = world.getTaskInfo(choice)
        print( str(info[0]) + ', will use ' + str(info[1]) + ' hours?') 
        confirm = input('"n" to cancel, enter to confirm')
        if confirm == 'n':
            pass
        else:
            world.performTask(choice)

    elif choice == 'status':
        print(player.getStatus())

    elif choice == 'help':
        print('Some available tasks are: ' + str(world.getTasks()) + 'status')
    

    elif choice == 'end':
        break


print('Game Over!')
print('You made it to day ' + str(world.getDayNumber()) + '!') 




