from modules.bot import Bot
from modules.input_handler import InputHandler
import time

def start_controller():
    print('Starting SNES controller..')

    input_handler = InputHandler()

    while True:
        input_handler.right()
        input_handler.left()
        input_handler.up()
        input_handler.down()
        time.sleep(1)
        

    # bot = Bot()
    # bot.run()

if __name__ == '__main__':
    start_controller()
