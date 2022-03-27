######################################################
# Project: 2
# UIN: 669794692
# repl.it URL: https://replit.com/@UICCS111HayesSpring2022/Project-2-SamuelShodiya#main.py

# For this project, I received help from the following members of CS111.
# Student1name, netID 12345678: help with background loop
# Student2name, netID 87654321: help with turtle heading and function parameters
 
######################################################

# imports
import turtle
import random
import data


def game_data_appearance(game):
  """shows remaining lives, score, and level on screen"""
  # Referencing turtle
  data.game_info["turtle"] = turtle.Turtle()
  t = data.game_info["turtle"]
  t.penup()
  t.goto(-180, 180)
  
  display_level = "level: " + str(game["level"]) 
  display_lives = "lives: " + str(game["lives"])

  t.write(str(display_level), font= ("Arial",  15, "normal"))

  t.penup()
  t.goto(-50, 180)
  t.write(str(display_lives), font= ("Arial",  15, "normal"))

  t.penup()
  t.goto(120, 180)

  display_scores = "Score: " + str(game["score"])
  t.write(str(display_scores), font= ("Arial",  15, "normal"))




  
# used as a parameter for in_collision function
objj_1 = data.animation_items[0]

def animation_loop(s, w, h):
  """Animation loop for the game objects."""
  for item in data.animation_items:
    # Referencing turtle
    item["turtle"] = turtle.Turtle()
    # print(item)
    # item["turtle"].hideturtle()
    item["turtle"].penup()

  # loop that runs through the game
  lives = data.game_info["lives"]
  
  while (lives > 0):

    # to clear previous drawings
    for item in data.animation_items:
      item["turtle"].clear()
    # harm objects movement across the screen
    for item in data.animation_items:
      if item["type"] == "harm":
        item["position"][1] += item["position_change"][1]  

    for item in data.animation_items:
      # edge condition for y values
      if (item["position"][1] < -(h/2)):
        item["position"][1] = h/2
      if (item["position"][1] > (h/2)):
        item["position"][1] = -(h/2)

      # edge condition for x values
      if (item["position"][0] > (w/2)):
        item["position"][0] = -(w/2)
      if (item["position"][0] < -(w/2)):
        item["position"][0] = w/2
        
    # collision detection
    for item in data.animation_items:
    #   # print(item)
      if item["type"] != "player" and item["type"] != "door":
        if (in_collision(objj_1, item) == True):
          print(in_collision(objj_1, item))
          # reducing live by 1
          data.game_info["lives"] -= 1
          lives = data.game_info["lives"]

          data.animation_items[0]['position'][0] = -w/2
          data.animation_items[0]['position'][1] = 0

          # Referencing turtle
          t = data.game_info["turtle"]
          t.clear()
          t.penup()
          t.goto(-180, 180)
          # calling function to write on screen
          game_data_appearance(data.game_info)
        
        # cheking collision for door
      if item["type"] != "player" and item["type"] != "harm":
      
        if (in_collision(objj_1, item) == True):
          print(in_collision(objj_1, item))
          # data.game_info["lives"] -= 1
          data.game_info["level"] += 1
          data.game_info["score"] += 1
          
          for item in data.animation_items:
            if item["type"] == "harm":
              item["position_change"][1] *= 2
          
          lives = data.game_info["lives"]
  
          data.animation_items[0]['position'][0] = -w/2
          data.animation_items[0]['position'][1] = 0
          data.animation_items[7]["position"][0] = w/2
          data.animation_items[7]["position"][1] = random.randint(-w/2, w/2)
          
          # data.game_info["turtle"] = turtle.Turtle()
          t = data.game_info["turtle"]
          t.clear()
          t.penup()
          t.goto(-180, 180)
          # calling function to write on screen
          game_data_appearance(data.game_info)

    # object appearance on the screen
    for item in data.animation_items:
      # showturtle
      item["turtle"].goto(item["position"])
      # method to show animated gif
      s.addshape(item["image"])
      item["turtle"].shape(item["image"])


    # update screen
    s.update()
    # Game over screen
  print("game over")
  for item in data.animation_items:
    
    
    
    game_score = "Game score: " + str(data.game_info["score"])
    game_level = "Level score: " + str(data.game_info["level"])

    # game score
    item["turtle"].penup()
    item["turtle"].goto(-50, 0)
    item["turtle"].hideturtle()
    item["turtle"].pencolor("indigo")
    item["turtle"].write(str(game_score), font = ("Arial", 15, "italic"))

    # level score
    item["turtle"].penup()
    item["turtle"].goto(-50, -40)
    item["turtle"].hideturtle()
    item["turtle"].pencolor("indigo")
    item["turtle"].write(str(game_level), font = ("Arial", 15, "italic"))

    # game over
    item["turtle"].penup()
    item["turtle"].goto(-50, 40)
    item["turtle"].hideturtle()
    item["turtle"].pencolor("red")
    item["turtle"].write("GAME OVER", font = ("Arial", 15, "normal"))



  
def in_collision (obj_1, obj_2):
  ''' checks whether two objects are touching (colliding) '''
  x_1 = obj_1["position"][0]
  y_1 = obj_1["position"][1]
  rad_x = obj_1["radius"]
  # print(x)
  x_2 = obj_2["position"][0]
  y_2 = obj_2["position"][1]
  rad_y = obj_2["radius"]

  dist_play_harm = ((x_1 - x_2)** 2 + (y_1 - y_2)**2)** .5
  # dist_play_harm = ["turtle"].distance(x,y)
  # print(dist_play_harm)
  raddi = rad_x + rad_y
# print(raddi)
# print(item["turtle"].distance(x,y))
  if (dist_play_harm <= raddi):
    print("Colliding\n")
    return True
  return False
  # elif (dist_play_harm > raddi):
  #   return False  




def main():
  """main function for the whole game"""
  s = turtle.Screen()
  s.setup(420,420)
  s.screensize(400,400)
  s.bgcolor("silver")
  s.bgpic("giphy-2.gif")
  s.tracer(0)
  w, h = s.screensize()

  # def show_coord(x, y):
  #   print(x, y)
  # s.onclick(show_coord)

  def up_key():
    """Player function to move up 5 uints"""
    data.animation_items[0]["position"][1] += 5
    # print(data.animation_items[0])
  def down_key():
    """Player function to down up 5 uints"""
    data.animation_items[0]["position"][1] -= 5
  def left_key():
    """Player function to Left up 5 uints"""
    data.animation_items[0]["position"][0] -= 5
  def right_key():
    """Player function to right up 5 uints"""
    data.animation_items[0]["position"][0] += 5

  # call to keypress functions
  s.onkey(up_key, "Up")
  s.onkey(down_key, "Down")
  s.onkey(left_key, "Left")
  s.onkey(right_key, "Right")
  s.listen()

  game_data_appearance(data.game_info)
  animation_loop(s, w, h)
  s.update()
  
main()
