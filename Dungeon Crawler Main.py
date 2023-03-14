from graphics import *
from characters import *
from walls import *

def main():
  win = GraphWin('Floor 1', 1000, 1000)
  win.setCoords(0, 0, 1000, 1000)

  background = Image(Point(500,500), "Floor_1.png")
  background.draw(win)

  name = input("What is your character's name? ")

  while len(name) > 11 or len(name) < 1:
    name = input("Name should be 1-10 characters: ")

  player = Player(name, win)

  skeleton_one = Image(Point(275, 125), "Skeleton_Image.png")
  skeleton_one.draw(win)

  action = input("Enter an action: ")
  movement = ['up','down','left','right','u','d','l','r']
  while action != 'done':
    if action.lower == 'Dead':
      player.death()
    elif action.lower() in movement:
      player.move(action)
      action = input("Enter an action: ")
    elif action.lower() == 'help':
      print('List of actions: Up, Down, Left, Right, Attack. You can also type the first letter of each action.')
      action = input("Enter an action: ")
    elif action.lower() == 'attack':
      target = player.closeEnemy()
      player.attack(target)
      action = input("Enter an action: ")
    else: 
      print("Invalid action. To get a list of actions, type 'help'.")
      action = input("Enter an action: ")
  
  

  
main()