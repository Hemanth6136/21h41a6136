import random, string
import webbrowser
import time

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
for i in range(10):
    webbrowser.open('https://www.bing.com/search?pglt=2337&q='+randomword(random.randint(0,100))+'&cvid=9eb3e57cb0b5434c9b51f0e6661b322b&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDEyMDJqMGoxqAIAsAIA&FORM=ANSPA1&PC=HCTS')
    time.sleep(7)