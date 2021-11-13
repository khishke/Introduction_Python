# pip install pg 
# or
# pip install PyGetWindow

# https://pyautogui.readthedocs.io/en/latest/keyboard.html
# https://pypi.org/project/PyGetWindow/
# https://www.theseattledataguy.com/4-simple-python-ideas-to-automate-your-workflow/#page-content
# https://linuxhint.com/gui_automation_pg/

# https://pg.readthedocs.io/en/latest/msgbox.html

import pyautogui as pg

# Open Matlab
pg.moveTo(100, 1060) 
pg.click()  
pg.write('Matlab')  # pg.write('Matlab', interval = 0.1)  
pg.press("enter")  

# play with Matlab
matW = pg.getWindowsWithTitle("Matlab")[0]
matW.minimize()
matW.restore()
matW.maximize()
matW.activate()
pg.getActiveWindowTitle()

# play with Chrome
chrW = pg.getWindowsWithTitle("Chrome")[0]
chrW.minimize()
chrW.restore()
chrW.maximize()
chrW.activate()
pg.getActiveWindowTitle() # pg.get+ functions

screenWidth, screenHeight = pg.size() # Total screen size
currentMouseX, currentMouseY = pg.position() # Returns two integers, the x and y of the mouse cursor's current position.
pg.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
pg.click() # Click the mouse at its current location.
pg.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
pg.click(button='right')
pg.move(0, 100)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
pg.doubleClick() # Double click the mouse at the
pg.moveTo(500, 500, duration=2, tween=pg.easeInOutQuad) # Use tweening/easing function to move mouse over 2 seconds.


spyW = pg.getWindowsWithTitle("Spyder")[0].activate()
spyW.resize(10, 10)
spyW.resizeTo(100, 100)

pg.hotkey('win','right')

pg.press(['ctrl','shift','left','left'])

pg.keyDown('ctrl')
pg.keyDown('shift')
pg.press('left')
pg.keyUp('shift')
pg.keyUp('ctrl')



# Message box
suggestion = 'Комьютероо унтрааж асаана уу.'
pg.alert(text = suggestion,title="Алдаа",button='Тийм')
pg.confirm('Shall I proceed?')
take = pg.confirm('Enter option.', buttons=['A', 'B', 'C'])
take = pg.prompt('What is your name?')
password = pg.password('Enter password (text will be hidden)')
    
    
    
import pg
im1 = pg.screenshot()
im1.save('my_screenshot.png')
im2 = pg.screenshot('my_screenshot2.png')
pg.screenshot('my_screenshot2.png',region=(0,0, 300, 400)) # left, top, width, and height

    
button7location = pg.locateOnScreen('my_screenshot2.png') # returns (left, top, width, height) of matching region
buttonx, buttony = pg.center(button7location)
    
    
buttonx, buttony = pg.locateCenterOnScreen('my_screenshot2.png') # returns (x, y) of matching region
pg.click(buttonx, buttony)  # clicks the center of where the button was found

# try
buttonx, buttony = pg.locateCenterOnScreen('ss.png') # returns (x, y) of matching region
pg.click(buttonx, buttony)  # clicks the center of where the button was found

