#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

from winreg import DeleteKey
import random

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Get to the Garden with a key and a potion to win! Avoid the monsters! Commands include go direction and get item.
    ''')

def description():
    """description of each room that describes every direction you can go"""
    if currentRoom == 'Hall':
        directions = 'You can go south or east.'
    elif currentRoom == 'Kitchen':
        directions = 'You can go north.'
    elif currentRoom == 'Dining Room':
        directions = 'You can go north, west, east, or south.'
    elif currentRoom == 'Garden':
        directions = 'You can go north.'
    elif currentRoom == 'Balcony':
        directions = 'You can go west.'
    else:
        directions = 'You can go south.'
    return directions
    
def showStatus():
    """determine the current status of the player"""
    print('---------------------------')
    # print number of moves
    print(f'Moves: {movesCounter}')
    # print the player's current location
    print('You are in the ' + currentRoom)
    # print available directions
    print(description())
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
## A dictionary linking a room to other rooms

rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'north' : 'Bathroom',
                  'west' : 'Hall',
                  'east' : 'Balcony',
                  'south': 'Garden',
                  'item' : 'potion'
               },
            'Garden' : {
                  'north' : 'Dining Room'
            },
            'Bathroom' : {
                    'south' : 'Dining Room'
            },
            'Balcony' : {
                'west' : 'Dining Room'
            }
         }


# start the player in the Hall
currentRoom = 'Hall'
movesCounter = 0

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            movesCounter += 1 # count the number of moves
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        print(f'Moves: {movesCounter - 1}')
        break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
