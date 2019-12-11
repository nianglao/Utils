# python3

# PyAutoGUI https://pyautogui.readthedocs.io/en/latest/introduction.html

import pyautogui
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
#pyautogui.moveTo(1300, 430)
btn_width = 1300
btn_height = 410

#pyautogui.moveTo(btn_width, btn_height)
# pyautogui.mouseDown()
# pyautogui.mouseUp()
pyautogui.screenshot(imageFilename='test.png', region=(1150, 200, 1050, 1350))
#pyautogui.click(x=btn_width, y=btn_height)
# pyautogui.screenshot('my_screenshot.png')
