
import random



def confirmAction(msg):
    print(msg)
    feedBack = input('"n" to cancel or enter to continue')
    if feedBack == 'n' or feedBack == 'N':
        return False
    else:
        return True




# https://www.w3schools.com/python/python_inheritance.asp
class UniversalProperties():
    def __init__(self):
        self.tasks = {}

    def getTasks(self):
        return list(self.tasks.keys())  # only return the task names

    def getTaskInfo(self, choice): # return the description and the time taken
        if choice in self.tasks:
            return self.tasks[choice]["description"] + ', will use ' + str(self.tasks[choice]['timeTaken']) + ' hours'
        else:
            return 'No such task'

    # def performTask(self): # Must add this function to each class

    # https://stackoverflow.com/questions/2612610/how-to-access-object-attribute-given-string-corresponding-to-name-of-that-attrib
    def useMaterials(self, materialsUsedDict):
        for mat in materialsUsedDict:
            print(mat)





class World(UniversalProperties): # Inherit functions from UniversalProperties
    def __init__(self):
        self.dayNight = "day"
        self.timeLeft = 12
        self.dayNumber = 1
        self.difficulty = 1 # Will ramp up very slowy over time, 1.02..
        self.luck = 1
        self.tasks = {
            "scout": ["Scouting increases your chances of finding nice things", 2], # "taskName:": ['description', timeTaken]
            "loot": ["Leave the base and search for useful things", 4]
        }


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


    def getTimeLeft(self):
        return self.timeLeft
    def getDayNight(self):
        return self.dayNight
    def getDayNumber(self):
        return self.dayNumber

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
            return 'Night sets upon you'
        else:
            self.dayNight = "day"
            self.dayNumber += 1 # if it's a new day add increment dayNumber
            self.difficulty += 0.02 # the world hates you
            return 'It is now day, number ' + self.dayNumber


    def useTime(self, timeTaken): # Check something doesn't take more time than you have, or progress dayNight if needed
        if timeTaken > self.timeLeft:
            self.changeDayNight()
            return 'It is now ' + self.dayNight
        else:
            self.timeLeft -= timeTaken
            return self.timeLeft

        
class Base(UniversalProperties):
    def __init__(self):
        self.health = 100
        self.barricades = 20
        self.defenseLevel = 0
        self.defenseMultiplier = 1
        self.craftLevel = 0
        self.toolLevel = 0
        self.materials = 13
        self.advancedMaterials = 5
        self.foodStored = 10
        self.waterStored = 100
        self.storage = []
        self.tasks = {
            "repairBarricades": {
                "description":"Use 3 materials to build up base defenses",
                "timeTaken": 3,
                "materialsUsed": {
                    "materials": 3
                }
            }, 
            "improveTools": { 
                "description": "Use 7 materials and 1 advanced material to improve your tools",
                "timeTaken": 3,
                "materialsUsed": {
                    "materials": 7,
                    "advancedMaterials": 1
                }
            },
            "craft": {
                "description": "Use 5 (minus tool level) materials to craft 1 advanced material",
                "timeTaken": 3,
                "materialsUsed": {
                    "materials": 5
                }
            }
        }

    def getBaseStatus(self):
        statusString = ('Health = ' + str(self.health) + ',\nBarricades = ' + str(self.barricades) + ',\nTool Level = ' + str(self.toolLevel) + ',\nMaterials = ' + str(self.materials) + ',\nAdvanced Materials = ' + str(self.advancedMaterials) + '\nFood Stroed= ' + str(self.foodStored) )
        return statusString

    def performTask(self, choice):
        if choice == 'repairBarricades':
            # self.materials -= 2
            self.materials -= self.tasks["repairBarricades"]["materialsUsed"]["materials"]
            self.barricades += 25
        elif choice == "improveTools":
            self.materials -= 3
            self.toolLevel += 1

    def getBase(self):
        baseString = ( '' )
        return baseString

    def repairBarricade(self, mulitplier):
        barricadeToAdd = round(random.randrange(8, 15) * mulitplier) + self.toolLevel
        self.barricades += barricadeToAdd


    def attackOnBase(self, attack):
        damageDone = round(attack - (self.defenseLevel * self.defenseMultiplier)) - self.defenseLevel
        self.barricades -= damageDone



class Player(UniversalProperties):
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
            "rest": ["heal", 2 ],
            "eat": ["drink food", 0.5],
            "drink": ["eat water", 0.5]
        }

    def performTask(self, choice):
        if choice == "rest":
            self.health += 10
            self.energy += 15
        elif choice == "eat":
            self.food += 20
            self.water += 10
            self.energy += 5
        elif choice == "drink":
            self.water += 20

    def getPlayerStatus(self):
        statusString = (self.name + ' the person,\nHealth = ' + str(self.health) + ',\nWater = ' + str(self.water) + ',\nFood = ' + str(self.food) + ',\nEnergy = ' + str(self.energy) + ',\nStatus = ' + str(self.status) + '\nInventory = ' + str(self.inventory) )
        return statusString
    
    # def dontLetOver100(self, stat):
    #     if self[stat] > 100:
    #         self[stat] = 100

        

    def setName(self, name):
        self.name = name
    


# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------

