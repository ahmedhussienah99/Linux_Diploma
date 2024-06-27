import pyautogui
import webbrowser
from time import sleep





webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
sleep(4)
location_search=pyautogui.locateOnScreen('points.png',confidence=0.9)
sleep(2)
pyautogui.moveTo(location_search.left+10,location_search.top+5)
sleep(2)
pyautogui.click(location_search.left+10,location_search.top+5)


sleep(2)
location_search=pyautogui.locateOnScreen('asread.png',confidence=0.9)
sleep(2)
pyautogui.moveTo(location_search.left+10,location_search.top+5)
sleep(2)
pyautogui.click(location_search.left+10,location_search.top+5)