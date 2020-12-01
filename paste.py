import argparse
import pyperclip
from input import KeyboardInput

DEFAULT_DELAY = 2.0

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--delay', metavar='N', type=int, help='Time delay to paste (in seconds)')
parser.add_argument('-t', '--text', help='Text to be typed')
parser.add_argument('-u', '--uppercase', action='store_true', help='Convert text to Uppercase')
args = parser.parse_args()

delay = args.delay or DEFAULT_DELAY
text = args.text or pyperclip.paste()

if args.uppercase:
    text = text.upper()

keyboard = KeyboardInput()
keyboard.type_string(text, delay)
