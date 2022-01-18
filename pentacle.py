from turtle import *
from time import *

# Variabler
tykkelse = 15
lengde = 300
grad = 144
farge1 = 'black'
farge2 = 'red'
 
 
#velger størrelse og farge på linje
pensize(tykkelse)
color(farge2)

# tegne pentacle med sirkel rundt:
forward(lengde)
left(grad)

forward(lengde)
left(grad)

forward(lengde)
left(grad)

forward(lengde)
left(grad)

forward(lengde)

#sort sirkel
left(72)
color(farge1)
circle(161)
sleep(3)
