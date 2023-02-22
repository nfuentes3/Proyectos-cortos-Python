"""Script automatico para mantener el cursor en movimiento e indicar coordenadas"""

import keyboard
import pyautogui as pa
import random
import time

while True: #Bucle infinito para que el script se corra constantemente
    pa.moveTo(x = random.randint(50,1900), y = random.randint(50,1000))
    time.sleep(1)
    print(pa.position())

    if keyboard.is_pressed('q'): #Tecla de escape del script
        break