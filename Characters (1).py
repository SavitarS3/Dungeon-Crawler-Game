from graphics import *
from walls import *

class Entity:
  def __init__(self, health: int, damage: int):
    self.health = health
    self.damage = damage
  
  def takeDamage(self, incoming_damage: int):
    self.health = self.health - incoming_damage
    # Add Damage Animation

  def heal(self, heal_amount: int):
    self.health += heal_amount

class Player(Entity):
  def __init__(self, name: str, win: GraphWin):
    self.name = name
    self.win = win

    self.player_starting_point_x = 475
    self.player_starting_point_y = 25

    self.current_point_x = self.player_starting_point_x
    self.current_point_y = self.player_starting_point_y

    self.image = Image(Point(self.current_point_x, self.current_point_y), "Player_Image.png")
    self.image.draw(self.win)

  def move(self, direction):
    if direction.lower() == 'up' or direction.lower() == 'u':
      for i in range(len(can_not_go_up)):
        can_go_up = True
        if self.current_point_x == can_not_go_up[i][0] and self.current_point_y == can_not_go_up[i][1]:
          can_go_up = False
          break
        else:
          pass
      if can_go_up == True:
        self.image.undraw()
        self.image = Image(Point(self.current_point_x, self.current_point_y + 50), "Player_Image.png")
        self.current_point_y += 50
        self.image.draw(self.win)
      else: 
        print("Up is not a viable action. Choose another action,")

    
    elif direction.lower() == 'down' or direction.lower() == 'd':
      for i in range(len(can_not_go_down)):
        can_go_down = True
        if self.current_point_x == can_not_go_down[i][0] and self.current_point_y == can_not_go_down[i][1]:
          can_go_down = False
          break
        else:
          pass
      if can_go_down == True:
        self.image.undraw()
        self.image = Image(Point(self.current_point_x, self.current_point_y - 50), "Player_Image.png")
        self.current_point_y -= 50
        self.image.draw(self.win)
      else: 
        print("Down is not a viable action. Choose another action.")


    elif direction.lower() == 'left' or direction.lower() == 'l':
      for i in range(len(can_not_go_left)):
        can_go_left = True
        if self.current_point_x == can_not_go_left[i][0] and self.current_point_y == can_not_go_left[i][1]:
          can_go_left = False
          break
        else:
          pass
      if can_go_left == True:
        self.image.undraw()
        self.image = Image(Point(self.current_point_x - 50, self.current_point_y), "Player_Image.png")
        self.current_point_x -= 50
        self.image.draw(self.win)
      else: 
        print("Left is not a viable action. Choose another action.")

      
    elif direction.lower() == 'right' or direction.lower() == 'r':
    
      for i in range(len(can_not_go_right)):
        can_go_right = True
        if self.current_point_x == can_not_go_right[i][0] and self.current_point_y == can_not_go_right[i][1]: 
          can_go_right = False
          break
        else:
          pass
      if can_go_right == True: 
        self.image.undraw()
        self.image = Image(Point(self.current_point_x + 50, self.current_point_y), "Player_Image.png")
        self.current_point_x += 50
        self.image.draw(self.win)
      else: 
        print("Right is not a viable action. Choose another action.")
  
  def attack(self, target: Entity):
    if (target.current_point_x - self.current_point_x == 50) or (target.current_point_y - self.current_point_y == 50) or (self.current_point_x - target.current_point_x == 50) or (self.current_point_y - target.current_point_y == 50):
      target.health -= self.damage

  def death(self):
    self.image.undraw()


class Enemy(Entity):
  def __init__(self, status):
    self.status = status