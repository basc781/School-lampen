from pynput.mouse import Button, Controller
import time

from selenium import webdriver

browser = webdriver.Chrome('/Users/bascouwenberg/Downloads/chromedriver')
# Hier open in het eerste lokaal met lamp
browser.get('https://p8verlicht3.fontys.nl/lweb802_pre/?project=App%20Ruimte%202%2C02.lweb2&address=P8VERLICHT3.fontys.nl&port=443&https=true#lvisPage')


mouse = Controller()
# Hier laat ik het programma eerst 5 seconde wachten zodat ik rustig op mijn plek kan gaan zitten
time.sleep(5)

print ("Current position: " + str(mouse.position))

# Hier verplaats ik de muis naar de nieuwe plek zodat hij de schuifbalk kan aanpassen
mouse.position = (200, 500)

mouse.move = (200,-103)

time.sleep(0.5)
# Hier laat ik hem op de nieuwe locatie klikken
mouse.click(Button.left, 1)
mouse.release(Button.left)
time.sleep(1)
# Hier laat ik hem weer naar een nieuwe locatie toe gaan dit gebeurd eigenlijk steeds opnieuw hieronder 
# alles is positie verandere en dan klikken loslaten en weer verplaatsen etc.
mouse.position = (200, 200)

mouse.move = (200,-103)
# de timers die hierop zitten zijn nog redelijk lang dit is omdat de browser het anders niet bij kon houden. 
time.sleep(1)
mouse.position = (200, 500)

mouse.move = (200,-103)

time.sleep(0.5)
mouse.click(Button.left, 1)
mouse.release(Button.left)
time.sleep(0.5)
mouse.position = (200, 200)

mouse.move = (200,-103)

time.sleep(1)
# En hier wissel ik van lokaal 
browser.get('https://p8verlicht3.fontys.nl/lweb802_pre/?project=App%20Ruimte%202%2C31.lweb2&address=P8VERLICHT3.fontys.nl&port=443&https=true#lvisPage')

mouse.position = (200, 500)

mouse.move = (200,-103)

time.sleep(1)
mouse.click(Button.left, 1)
mouse.release(Button.left)
time.sleep(0.5)
mouse.position = (200, 200)

mouse.move = (200,-103)

time.sleep(0.5)
mouse.position = (200, 500)

mouse.move = (200,-103)


time.sleep(0.5)
mouse.click(Button.left, 1)
mouse.release(Button.left)
time.sleep(0.5)
mouse.position = (200, 200)

mouse.move = (200,-103)
