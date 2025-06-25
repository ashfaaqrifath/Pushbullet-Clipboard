import pyperclip
from pushbullet import Pushbullet


pb = Pushbullet("o.zOGSadXlTdisBBYdz5HlpDoxmUe0jBdR")

def pushbullet_notification(send):
    
    pb.push_note("",send)


def clipboard():
    
            text = pyperclip.paste()
            pushbullet_notification(text)
            

clipboard()
