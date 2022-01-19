from turtle import *
from time import *

#variabler
tykkelse = 10
lengde_1 = 255

farge_1 = 'blue'
farge_2 = 'green'
farge_3 = 'red'
pensize(tykkelse)

for i in range(6):
	if i==0:
		left(60) # a - g
		color('black')
		forward(lengde_1)
		sleep(1)
	elif i==1:
		left(150) #g - j
		color('black') 
		forward(lengde_1)
		sleep(1)
	elif i==2:
		right(150) # j - h
		color('black')
		forward(lengde_1)
		sleep(1)
	elif i==3:
		right(128) # h - d (ish..)
		color('black')
		forward(lengde_1)
		sleep(1)
	elif i==4:
		right(150) # d - i
		color('black')
		forward(lengde_1)
		sleep(1)
	elif i== 5:
		left(145) # i - a
		color('black')
		forward(245)
		sleep(15)
	
		


