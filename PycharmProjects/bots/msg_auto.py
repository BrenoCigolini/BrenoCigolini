import pyautogui as py
import random
import time

time.sleep(5)

mensagens = ['macaco']
for i in range(50):
#while True:
    msg = random.choice(mensagens)
    py.write(msg)
    py.press('enter')
