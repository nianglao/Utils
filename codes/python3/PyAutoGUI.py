# python3

# PyAutoGUI https://pyautogui.readthedocs.io/en/latest/introduction.html

import pyautogui
screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
#pyautogui.moveTo(1300, 430)


def next_page():
    btn_width = 1240
    btn_height = 430
    pyautogui.moveTo(btn_width, btn_height)
    pyautogui.mouseDown()
    pyautogui.mouseUp()


total = 1
output_dir = 'screenshots'
for i in range(total):
    print('screen shot on page %d' % (i + 1))
    pic_name = '%s/%s.png' % (output_dir, i + 1)
    pyautogui.screenshot(imageFilename=pic_name,
                         region=(1165, 150, 1040, 1400))
    next_page()
#pyautogui.click(x=btn_width, y=btn_height)
# pyautogui.screenshot('my_screenshot.png')
