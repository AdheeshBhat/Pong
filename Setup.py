from audioop import add
from processing_py import*
import random
import keyboard
import time
app = App(1920,1024)

#class for pong paddles
class paddle:
  x = 850
  y = 900
game_paddle = paddle()
#starting position for ball
ball_x = 900
ball_y = 50
#changes direction of ball
global X_DIRECTION
global Y_DIRECTION
global SCORE
global list_item1
global list_item2
global list_item3
global list_item4
global list_item5
global current_time
global time_limit
global low_gravity
global ball_speed
global low_gravity_text
global text_time_limit
global double_score_text
global double_score_time_limit
global double_score_text_time_limit
global score_counter
global score_powerup_checker
global main_menu
#This is used to change the direction of the ball
X_DIRECTION = 1
Y_DIRECTION = 1
low_gravity = False
main_menu = True
score_counter = 1
score_powerup_checker = False
double_score_text_time_limit = -1
double_score_text = False
current_time = time.time()
double_score_time_limit = -1
text_time_limit = -1
low_gravity_text = False
ball_speed = 10
current_time = time.time()
time_limit = -1
SCORE = 0
#Used to insert top five scores on the screen
global TO_INSERT
TO_INSERT = 0
#displays highest score
global HIGHEST_SCORE
HIGHEST_SCORE = 0
#top five highest scores
global TOP_FIVE
TOP_FIVE = [0] * 5
movement_direction = 5
list_item1 = "0"
list_item2 = "0"
list_item3 = "0"
list_item4 = "0"
list_item5 = "0"
#powerup cube
powerup_cube_x = random.randint(100,1700)
powerup_cube_y = random.randint(100,800)
app.rect(powerup_cube_x, powerup_cube_y, 100, 100)
#powerup cube 2
powerup_cube2_x = random.randint(100,1700)
powerup_cube2_y = random.randint(100,800)
app.rect(powerup_cube2_x, powerup_cube2_y, 100, 100)