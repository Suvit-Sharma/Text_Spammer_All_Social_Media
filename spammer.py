import pyautogui
import time

time.sleep(5)

pyautogui.typewrite("omae wa mou shindeiru 😊".upper())
pyautogui.press("enter")
time.sleep(5)

pyautogui.typewrite("HUMSHAKALS SCRIPT...... here we go 😊".upper())
pyautogui.press("enter")

time.sleep(5)

f = open("text.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(0.3)


