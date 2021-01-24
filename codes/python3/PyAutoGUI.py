import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
print('screen size: length %d, height %d' % ( screenWidth, screenHeight))

#loc_pic = 'loc_pic.png'
#loc = pyautogui.locateOnScreen(loc_pic, True)
#print('location of pic %s is %s' % (loc_pic, loc))
# 
#pyautogui.moveTo(1300, 430)
def move_mouse_to(pos):
    print('move to position: x=%d, y=%d'%(pos.x, pos.y))
    btn_width = pos.x
    btn_height = pos.y
    pyautogui.moveTo(btn_width, btn_height)

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900
TOP_LEFT = Pos(0, 0)
BOTTOM_RIGHT = Pos(SCREEN_WIDTH, SCREEN_HEIGHT)

move_mouse_to(Pos(66, 182))
#move_mouse_to(Pos(594, 842))

top_left = Pos(70, 178)
bottom_right = Pos(598, 838)
width = bottom_right.x - top_left.x
height = bottom_right.y - top_left.y

width = width * 2
height = height * 2
print('width: %d, height: %d'%(width, height))

top_left.x = top_left.x * 2
top_left.y = top_left.y * 2

def sleep():
    ts = 1
    print('sleep %d s'%ts)
    time.sleep(ts)

def next_page():
    btn_width = 637
    btn_height = 695
    pyautogui.click(btn_width,btn_height)
    #pyautogui.doubleClick(btn_width,btn_height)
    #pyautogui.moveTo(btn_width, btn_height)
    #pyautogui.mouseDown()
    sleep()
    #pyautogui.mouseUp()
    #pyautogui.moveTo(601, 604)
    #pyautogui.mouseDown()
    #pyautogui.mouseUp()
    


total = 280
output_dir = 'tmp'
for i in range(total):
    pic_name = '%s/%s.png' % (output_dir, i + 1)
    pyautogui.screenshot(imageFilename=pic_name,region=(top_left.x, top_left.y, width, height))
    print('screen shot on page %d, output to %s' % (i + 1, pic_name))
    next_page()
#pyautogui.click(x=btn_width, y=btn_height)
# pyautogui.screenshot('my_screenshot.png')
