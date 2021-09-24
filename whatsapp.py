import pyautogui

x = 0
pyautogui.moveTo(690, 962, 1)
while (x < 10):
    
    #go to name
    
    #scroll down
    pyautogui.scroll(-25)
    pyautogui.moveTo(690, 962, 1)
    #right click on name
    pyautogui.click(button='right', clicks=1, interval=0.25)
    #move to inspect
    pyautogui.moveTo(775, 932, 1)
    #left click inspect
    pyautogui.click(button='left')
    #go to selected text in inspect tab
    pyautogui.moveTo(1568, 321, 1)
    #right click to open menu
    pyautogui.click(button='right', clicks=1, interval=0.25)
    #go to copy
    pyautogui.moveTo(1690, 530, 1)
    #left click copy
    pyautogui.click(button='left')
    #go to copy element
    pyautogui.moveTo(1397, 570, 1)
    #left click copy element
    pyautogui.click(button='left')
    #go to notepad top right
    pyautogui.moveTo(1086, 835, 1)
    #left click
    pyautogui.click(button='left')
    #right click
    pyautogui.click(button='right', clicks=1, interval=0.25)
    #go to Paste
    pyautogui.moveTo(1143, 532, 1)
    #left click
    pyautogui.click(button='left')
    #press enter
    pyautogui.press('enter')
    pyautogui.moveTo(690, 962, 1)
    x = x+1



