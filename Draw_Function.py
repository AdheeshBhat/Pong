import Setup
import keyboard
import Ball_Movement
import Key_Commands
import time
import Top_Five_Scores
from processing_py import*

#draw function
while True:
  if not Setup.main_menu:
    Setup.current_time = time.time()
    if Setup.current_time >= Setup.text_time_limit:
      Setup.low_gravity_text = False

    Setup.current_time = time.time()
    if Setup.current_time >= Setup.time_limit:
      Setup.low_gravity = False

    Setup.current_time = time.time()
    if Setup.current_time >= Setup.double_score_text_time_limit:
      Setup.double_score_text = False

    if Setup.current_time >= Setup.double_score_time_limit:
      Setup.score_powerup_checker = False

    Setup.app.background(255,255,255)
    #paddle
    Setup.app.fill(0,0,0)
    Setup.app.rect(Setup.game_paddle.x,Setup.game_paddle.y,150,20)
    Setup.app.ellipse(Setup.ball_x,Setup.ball_y,50,50)
    
    Top_Five_Scores.top_five()
    Key_Commands.key_commands()
    Setup.ball_x, Setup.ball_y = Ball_Movement.ball_movement(Setup.movement_direction,Setup.ball_x, Setup.ball_y)
    #scoreboard
    Setup.app.fill(73,163,242)
    Setup.app.rect(1650, 20, 250, 100, 10)
    Setup.app.fill(0,0,0)
    Setup.app.textSize(20)
    Setup.app.text("Score = " + str(Setup.SCORE), 1700, 40)
    Setup.app.fill(Setup.random.randint(0,255), Setup.random.randint(0,255), Setup.random.randint(0,255))
    Setup.app.rect(Setup.powerup_cube_x, Setup.powerup_cube_y, 100, 100)
    Setup.app.fill(50,50,50)
    Setup.app.rect(Setup.powerup_cube2_x, Setup.powerup_cube2_y, 100, 100)
    #writes low gravity text on screen
    if Setup.low_gravity_text:
      Setup.app.textSize(50)
      Setup.app.text("Low Gravity", 800, 500)

    if Setup.double_score_text:
      Setup.app.textSize(50)
      Setup.app.text("Double Score", 800, 500)

  if Setup.main_menu:
    Key_Commands.key_commands()
    Setup.app.background(63,149,224)
    Setup.app.fill(255,255,255)
    Setup.app.rect(750, 90, 400, 200, 10)
    Setup.app.textSize(80)
    Setup.app.fill(0,0,0)
    Setup.app.text("Pong", 850, 200)
    Setup.app.fill(255,255,255)
    Setup.app.rect(650, 600, 600, 270, 10)
    Setup.app.textSize(80)
    Setup.app.fill(0,0,0)
    Setup.app.text("Press P to Play", 670, 750)
#(800,700)

  Setup.app.redraw()