from input import KeyboardInput
import subprocess

def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

text = str(getClipboardData())
text = text[2:-1]

delay = float(2)

keyboard = KeyboardInput()
keyboard.type_string(text, delay)