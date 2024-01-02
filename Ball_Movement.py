#Ball_Movement: This file allows the ball to move around the screen and hit
# the powerup cubes and paddles. It also has the top five scoreboard.
#
import Setup
import random
import time
#moves the ball around the screen
def ball_movement(movement_direction, ball_x, ball_y):
  global X_DIRECTION
  global Y_DIRECTION
  global SCORE
  global HIGHEST_SCORE
  global TO_INSERT
  global TOP_FIVE
  global list_item1
  global list_item2
  global list_item3
  global list_item4
  global list_item5


#if the ball hits either side of the screen, it bounces back
  if Setup.ball_x - 25 >= 1920 or 0 >= Setup.ball_x - 25:
    Setup.X_DIRECTION *= -1
  if Setup.ball_y - 25 <= 0:
    Setup.Y_DIRECTION *= -1

#if the ball goes under the paddle, reset the game and score.
  if Setup.ball_y + 25 >= 1024:
    Setup.ball_x = 900
    Setup.ball_y = 50
    Setup.game_paddle.x = 850
    Setup.game_paddle.y = 900
    HIGHEST_SCORE = Setup.SCORE
    #car = ""
    

    #goes through list of top five high scores
    for i in range(len(Setup.TOP_FIVE)):
      #if the highest score is greater than the score in TOP_FIVE, add score to "TO_INSERT"
      if HIGHEST_SCORE >= Setup.TOP_FIVE[i]:
        Setup.TO_INSERT = Setup.TOP_FIVE[i]
        Setup.TOP_FIVE[i] = HIGHEST_SCORE
        HIGHEST_SCORE = Setup.TO_INSERT
    Setup.list_item1 = str(Setup.TOP_FIVE[0])
    Setup.list_item2 = str(Setup.TOP_FIVE[1])
    Setup.list_item3 = str(Setup.TOP_FIVE[2])
    Setup.list_item4 = str(Setup.TOP_FIVE[3])
    Setup.list_item5 = str(Setup.TOP_FIVE[4])
    Setup.SCORE = 0
  #if there is low gravity, speed is halfed.
  if Setup.low_gravity:
    Setup.ball_speed = 2
  else:
    Setup.ball_speed = 10
  

  #if the direction of the ball is down, move the ball down
  Setup.ball_y += Setup.ball_speed * Setup.Y_DIRECTION
  Setup.ball_x += Setup.movement_direction * Setup.X_DIRECTION


  #if the ball hits the powerup cube 1, it bounces back and the powerup is enabled.   
  if Setup.powerup_cube_x <= Setup.ball_x + 25:
    if (Setup.ball_x - 25 <= Setup.powerup_cube_x + 100):
      if ((Setup.powerup_cube_y + 100) >= Setup.ball_y - 25 and Setup.ball_y + 25 >= Setup.powerup_cube_y):
        Setup.time_limit = Setup.current_time + 5
        Setup.low_gravity = True
        Setup.ball_y -= 25
        Setup.Y_DIRECTION *= -1
        Setup.powerup_cube_x = random.randint(100,1700)
        Setup.powerup_cube_y = random.randint(100,800)
        Setup.text_time_limit = Setup.current_time + 3
        Setup.low_gravity_text = True
    
    #if the ball hits the powerup cube 2, the powerup is enabled.
    if Setup.powerup_cube2_x <= Setup.ball_x + 25:
      if (Setup.ball_x - 25 <= Setup.powerup_cube2_x + 100):
        if ((Setup.powerup_cube2_y + 100) >= Setup.ball_y - 25 and Setup.ball_y + 25 >= Setup.powerup_cube2_y):
          Setup.double_score_time_limit = Setup.current_time + 30
          Setup.double_score_text_time_limit = Setup.current_time + 3
          Setup.score_powerup_checker = True
          Setup.powerup_cube2_x = random.randint(100,1700)
          Setup.powerup_cube2_y = random.randint(100,800)
          Setup.double_score_text = True


  #if the ball hits the paddle, change direction
  if (Setup.game_paddle.x <= Setup.ball_x + 25):
    if Setup.ball_x - 25 <= (Setup.game_paddle.x + 150) and ((Setup.game_paddle.y - 50) <= Setup.ball_y - 25 <= Setup.game_paddle.y):
      Setup.ball_y -= 25
      Setup.Y_DIRECTION *= -1
      Setup.SCORE += 1
      Setup.app.rect(Setup.powerup_cube_x, Setup.powerup_cube_y, 100, 100)
      if Setup.score_powerup_checker:
        Setup.SCORE += Setup.score_counter
   
  return Setup.ball_x, Setup.ball_y
def mousePressed():
  print (mousePressed.mouseY)