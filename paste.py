import argparse
import subprocess

from input import KeyboardInput


def getClipboardData():
    p = subprocess.Popen(['xclip', '-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--delay', metavar='N', type=int, help='Time delay to paste')
args = parser.parse_args()

delay = args.delay or float(2)

text = str(getClipboardData())
text = text[2:-1]

keyboard = KeyboardInput()
keyboard.type_string(text, delay)
