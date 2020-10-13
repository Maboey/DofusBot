import DofusBot as db
import FakeInput as FI
import time
import random

run = True
play = False
readyToChangeZone = False
screenSize = FI.GetScreenSize()
timeStampTriedChangingZone = time.time()
waitZoneChange = 10 # time between two tries of zone travels 
zoneLoading = False
botTraveling = True

print("ScreenSize : X = ", str(screenSize[0]),", Y = ", str(screenSize[1]))
print("Bot Ready")

while run :
    #if bot is not paused
    if play:
        if botTraveling:
            if readyToChangeZone :
                db.ChangeZone(random.choice(["up","down","left","right"]))
                readyToChangeZone = False
                timeStampTriedChangingZone = time.time()
            else :
                if db.DetectZoneLoading:
                    zoneLoading = True
                else:
                    zoneLoading = False
                if (time.time() >= (timeStampTriedChangingZone + waitZoneChange)) or (zoneLoading and db.DetectZoneLoaded()):
                    zoneLoading = False
                    readyToChangeZone = True

    #pause or stop bot detection
    if db.PausePlay():
        play = not play
        if play:
            print("Bot Resumed")
        else:
            print("Bot Paused")
    if db.StopBot():
        run = False
        print("Bot Stopped")