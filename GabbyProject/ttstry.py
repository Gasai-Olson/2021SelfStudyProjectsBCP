from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from tts import call
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")



# enable browser logging
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome('/Users/timyc1/Desktop/Gabby/chromedriver')

# load the desired webpage

file = "/Users/timyc1/Desktop/Gabby/GabbiesMakerBoard.html"
driver.get("file://" + file)

# print messages
while True:
    for entry in driver.get_log('browser'):
            current = str(entry)
            for i in range(4):
                trashvar, current = current.split(":",1)
            trashvar,current = current.split(" ",1)
            current,trashvar = current.split("'",1)
            current = current.replace('"','')
            if 'net' in current:
                pass
            else:
                call(current)