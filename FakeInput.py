"""
Fake Input
"""
from win32api import GetSystemMetrics
import keyboard
import mouse
from PIL import ImageGrab
import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = os.getcwd() + "/Tesseract/tesseract.exe"

"""
GetcreenSize()
retourne la taille de l'écran en x y
"""
def GetScreenSize():
    screenSize = [GetSystemMetrics(0),GetSystemMetrics(1)]
    return screenSize

"""
=== ClickXY(x,y,moveDuration) ===
Simule un click en position x y avec une délai pour le mouvement
"""
def ClickXY(x,y,moveDuration):
    mouse.move(x,y,True,moveDuration)
    mouse.click()

"""
=== KeyboardInput(k_input) ===
 Simule la pression d'une touche
"""
def KeyboardInput(k_input): 
    keyboard.press_and_release(k_input)

"""
=== GetScreenPixels() ===
retourne un tableau 2d de pixel [RGB]
"""
def GetScreenPixels(): 
    image = ImageGrab.grab()
    return image.load()

"""
=== ReadTextOnScreen() ===
retourne le texte à l'écran sous forme de string
"""
def ReadTextOnScreen():
    image = ImageGrab.grab()
    return pytesseract.image_to_string(image)