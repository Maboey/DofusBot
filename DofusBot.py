import FakeInput as FI
import keyboard
import time
import random

#Detects if ',' is pressed
def StopBot():
    if keyboard.is_pressed(','):
        time.sleep(0.5)
        return True
    else:
        return False

#Detects if '.' is pressed
def PausePlay():
    if keyboard.is_pressed('.'):
        time.sleep(0.5)
        return True
    else:
        return False

def ChangeZone(direction):
    screenSize = FI.GetScreenSize()
    if direction == "left":
        x = random.randrange(screenSize[0]//9,screenSize[0]//8)
        y = random.randrange(screenSize[1]//6*2,screenSize[1]//6*5)
        FI.ClickXY(x,y,0.1)
    if direction == "right":
        x = random.randrange(screenSize[0]//8*7,screenSize[0])
        y = random.randrange(screenSize[1]//6*2,screenSize[1]//6*5)
        FI.ClickXY(x,y,0.1)
    if direction == "up":
        offsetY = screenSize[1]//45
        offsetX = screenSize[0]//7
        x = random.randrange(offsetX,screenSize[0]-offsetX)
        y = random.randrange(offsetY,screenSize[1]//28)
        FI.ClickXY(x,y,0.1)
    if direction == "down":
        offsetX = screenSize[0]//7
        x = random.randrange(offsetX,screenSize[0]-offsetX)
        y = random.randrange(screenSize[1]//6*5,screenSize[1]//7*6)
        FI.ClickXY(x,y,0.1)

def DetectZoneLoading():
    zoneLoading = True
    screenSize = FI.GetScreenSize()
    screenCenter = [screenSize[0]//2,screenSize[1]//2]
    radiusToCheck = 10
    screenPixels = FI.GetScreenPixels()
    startingX = screenCenter[0]-radiusToCheck
    startingY = screenCenter[1]-radiusToCheck
    for Area in range(2*radiusToCheck):
        if screenPixels[startingX+Area,startingY+Area] != [0,0,0]:
            zoneLoading = False
            break
    return zoneLoading


    
def DetectZoneLoaded():
    zoneLoaded = True
    screenSize = FI.GetScreenSize()
    screenCenter = [screenSize[0]//2,screenSize[1]//2]
    radiusToCheck = 50
    screenPixels = FI.GetScreenPixels()
    startingX = screenCenter[0]-radiusToCheck
    startingY = screenCenter[1]-radiusToCheck
    for Area in range(2*radiusToCheck):
        if screenPixels[startingX+Area,startingY+Area] != [0,0,0]:
            zoneLoaded = False
            break
    return zoneLoaded