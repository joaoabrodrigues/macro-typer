from tkinter import *
from functools import partial
from input import KeyboardInput
import subprocess

def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

text = str(getClipboardData())
text = text[2:-1]

keyboard = KeyboardInput()
keyboard.type_string(text, float(2))