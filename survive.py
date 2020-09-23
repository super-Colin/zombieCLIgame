
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
            "rest": "Helps you heal, recover energy",
            "build": "Use materials to improve your base",
            "scout": "Scouting increases your chances of finding nice things",
            "loot": "Leave the base and search for useful things"
        } 


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

    def dayTask(self, choice):
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

    def repairBarricade(self, mulitplier):
        barricadeToAdd = round(random.randrange(8, 15) * mulitplier) + self.toolLevel
        self.barricade += barricadeToAdd


    def attackOnBase(self, attack):
        damageDone = round(attack - (self.defenseLevel * self.defenseMultiplier)) - self.defenseLevel
        self.barricade -= damageDone



class Player:
    def __init__(self):
        self.name = ''
        self.health = 100
        self.water = 100
        self.food = 100
        self.energy = 100
        self.status = "Healthy & Happy"
        self.workMultiplier = 1
        self.inventoryMax = 8
        self.inventory = []

    def setName(self, name):
        self.name = name

    






world = World()
base = Base()
player = Player()


print('Welcome to Zombie Survival Game')
player.name = input('Player Name: ')
print(player.name)


print('There are zombies and shit outside so making trips outside is always risky')
print('You can always use "help" to find out more')

print('You find yourself in an abandoned old house.')




print("During the day it's safer to stay inside and work on your base")
print("During the night it's easier so sneak to locations for supplies, but your base is more likely to be attacked")




# while base.health > 0:

choice = input('What would you like to do?')

if world.dayNight == 'day':
    print("It's day")

    if world.timeLeft == 0:
        print('The day is over')


if world.dayNight == 'night':
    print("it's day")

    if world.timeLeft == 0:
        print('The night is over')

