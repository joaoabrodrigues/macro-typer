from input import KeyboardInput
import subprocess
import clipboard

text = str(clipboard.paste())

keyboard = KeyboardInput()
keyboard.type_string(text)