#Seaver Olson 2021
import rumps
import random
from rumps.rumps import quit_application
import os

rumps.debug_mode(True)

def sad_message():
    l = {'Awww you closed me :(' : 'Sorry','Catastrophic Error: you closed your favorite app' : 'OH NO',
        'User Error: Please replace user' : 'Burn',
            'OSDA has alerted Apple of your anti-Steve Jobs energy, please proclaim Steve Jobs as the second coming of christ in order to countinue' : 'Heil Steve Jobs',
    }
    message, okay = random.choice(list(l.items()))
    return message, okay

class OSDAApp(rumps.App):
    def __init__(self):
        super(OSDAApp, self).__init__("OSDA")
        self.menu = ["Text Interface", "Help", "Close"]
        self.quit_button=None

    @rumps.clicked("Text Interface")
    def text_interface(self,trash):
        os.system('python3.8 /Users/timyc1/Desktop/houseofrep/UI.py')
    
    @rumps.clicked('Help')
    def help(self,event=None):
        os.system('open /Users/timyc1/Desktop/houseofrep/home.html')

    @rumps.clicked("Close")
    def close_thingy(notification_argument,quit_argument):
        message, okay = sad_message()
        rumps.alert(message = message, ok=okay)
        rumps.quit_application()
        
while __name__ == '__main__':
    App = OSDAApp()
    App.run()


    

    
