import Setup
import keyboard
import mouse
#movement for the paddle
def key_commands():
    if Setup.keyboard.is_pressed("a") and Setup.game_paddle.x >= 0 + 10:
        Setup.game_paddle.x -= 10
    if keyboard.is_pressed("d") and Setup.game_paddle.x + 150 <= 1920 - 10:
        Setup.game_paddle.x += 10
    if keyboard.is_pressed("p") or keyboard.is_pressed("P") and Setup.main_menu:
        Setup.main_menu = False