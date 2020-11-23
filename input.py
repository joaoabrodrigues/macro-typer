from pynput.keyboard import Key, Controller
import time

class KeyboardInput:

    def type_string(self, value):
        keyboard = Controller()
        time.sleep(0.5)
        keyboard.type(value)
