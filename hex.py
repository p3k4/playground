from turtle import *
from time import *
from math import *

##-----------Forsøk på å finne koordinater til 30 graders vinkler basert på omriss-radius -------##
#
# a = x
# b = y
# r = sirkel radius.
# x-verdi
# a = int(r*cos(30))
#
# y-verdi
# b = int((r*sin((30))))
#
##-------------------------------------------------------------------------##

## Omtrent riktig, men ut ifra øyemål og dermed ikke presist.
#globale variabler
t = 10
l = 300
pensize(t)

#do stuff..
for i in range(6):
	if i==0:
		left(60) # a - g
		forward(l)
		sleep(1)
	elif i==1:
		left(148) #g - j
		forward(l)
		sleep(1)
	elif i==2:
		right(150) # j - h
		forward(l)
		sleep(1)
	elif i==3:
		right(128) # h - d (ish..)
		forward(l)
		sleep(1)
	elif i==4:
		right(150) # d - i
		forward(l)
		sleep(1)
	elif i== 5:
		left(145) # i - a
		forward(l)
		sleep(15)
	
		

