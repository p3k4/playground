from turtle import *
from time import *
from math import *

##-----------Forsøk på å finne koordinater til 30 graders vinkler basert på omriss-radius -------##
# https://bit.ly/3tKLuSr <-- Link, matematikker fra Youtube som viser dette som en mulig løsning.
# a = x
# b = y
# r = sirkel radius.
# x-verdi
# a = int(r*cos(30))
#
# y-verdi
# b = int((r*sin((30))))
#
##-----------------------------------------------------------------------------------------------##

## Omtrent riktig, men gjort ifra øyemål og dermed ikke presist.
#globale variabler
t = 10
l = 300
pensize(t)

#do stuff..
for i in range(6):
	if i==0:
		left(60) # punkt a
		forward(l)
		sleep(1)
	elif i==1:
		left(148) # punkt b
		forward(l)
		sleep(1)
	elif i==2:
		right(150) # punkt c
		forward(l)
		sleep(1)
	elif i==3:
		right(128) # punkt d
		forward(l)
		sleep(1)
	elif i==4:
		right(150) # punkt e
		forward(l)
		sleep(1)
	elif i== 5:
		left(145) # punkt f
		forward(l)
		sleep(15)
