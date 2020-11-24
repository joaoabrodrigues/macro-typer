import time

from pynput.keyboard import Controller


class KeyboardInput:

    @staticmethod
    def type_string(value, delay=0):
        keyboard = Controller()
        time.sleep(delay)
        keyboard.type(value)
