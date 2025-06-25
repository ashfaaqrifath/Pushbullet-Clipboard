import pyperclip
from pushbullet import Pushbullet
import keyboard

pb = Pushbullet("API TOKEN")

def pushbullet_notification(send):
    pb.push_note("", send)

def clipboard():
    while True:
        keyboard.wait("ctrl+b")
        text = pyperclip.paste()
        pushbullet_notification(text)

clipboard()