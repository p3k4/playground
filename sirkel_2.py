#legger til biblioteker. De uten om standard-bibliotekene må allerede være installert på maskinen!
from turtle import *
from time import *

pensize(20) # øker linjetykkelse
color('purple') # velger første farge
circle(40) # tegner første sirkel med radius 40
sleep(2) #Venter med å kjøre neste linje etter gitt antall sekund sendt med som parameter.

#endrer linjefarge etter regnbuens farger og øker radius med 10 for hver nye sirkel som blir tegnet.
#ventetiden er alltid 2 sekunder.
color('indigo')
circle(50)
sleep(2)

color('blue')
circle(60)
sleep(2)

color('green')
circle(70)
sleep(2)

color('yellow')
circle(80)
sleep(2)

color('orange')
circle(90)
sleep(2)

color('red') 
circle(100)
sleep(2)

