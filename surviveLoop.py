from surviveBackend import World, Base, Player

# ------------------------------------------------------------------
# ------------------------------------------------------------------
# ------------------------------------------------------------------

world = World()
base = Base()
player = Player()


# print('Welcome to Zombie Survival Game')
# playerName = input('Player Name: ')
# plyer.setName(playerName)

# print('There are zombies and shit outside so making trips outside is always risky')
# print('You can always use "help" to find out more')

# print("During the day it's safer to stay inside and work on your base")
# print("During the night it's easier so sneak to locations for supplies, but your base is more likely to be attacked")

# print('You find yourself in an abandoned old house.')


while base.health > 0:

    print('\nIt is currently ' + world.getDayNight() + ' on day# ' + str(world.getDayNumber()) )
    choice = input( "What would you like to do? (\"help\" if you're lost, \"end\" to quit)\n")

    if choice in world.getTasks():
        # info = world.getTaskInfo(choice)
        # print( str(info[0]) + ', will use ' + str(info[1]) + ' hours?') 
        print(world.getTaskInfo(choice))
        confirm = input('"n" to cancel, enter to confirm')
        if confirm == 'n':
            pass
        else:
            world.performTask(choice)

    if choice in base.getTasks():
        # info = base.getTaskInfo(choice)
        # print( str(info[0]) + ', will use ' + str(info[1]) + ' hours?') 
        print(base.getTaskInfo(choice))
        confirm = input('"n" to cancel, enter to confirm')
        if confirm == 'n':
            pass
        else:
            base.performTask(choice)

    if choice in player.getTasks():
        # info = player.getTaskInfo(choice)
        # print( str(info[0]) + ', will use ' + str(info[1]) + ' hours?') 
        print(player.getTaskInfo(choice))
        confirm = input('"n" to cancel, enter to confirm')
        if confirm == 'n':
            pass
        else:
            player.performTask(choice)

    elif choice == 'status':
        print(player.getStatus())

    elif choice == 'help':
        print('Some available tasks are: ' + str(world.getTasks()) + str(base.getTasks()) + str(player.getTasks()) )
    

    elif choice == 'end':
        break


print('Game Over!')
print('You made it to day ' + str(world.getDayNumber()) + '!') 




