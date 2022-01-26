from turtle import *
from math import *
from time import *

## info
# Kiss - ansiksmaske
#tegnes fra venstre til høyre: Paul, Peter, Ace, Gene.

## globale variabler/setup

# endre skjerm størrelse
screensize()
setup(width = 0.5, height = 1.0)
pen10 = 8


## startpunkt for å tegne del 1
def start_1():
	penup()
	home()
	left(100)

def del_1_fill():
	pensize(pen10)
	pendown()
	begin_fill()
	circle(800,30)
	right(130)
	forward(340)
	right(128.7)
	circle(800,29.5)
	end_fill()
	penup()

def start_2():
	home()
	goto(-175.01,375.31)
	left(180)
	forward(45)
	left(55)

def del2():
	pendown()
	pensize(pen10)
	begin_fill()
	circle(640,35)
	circle(250,22)
	
	circle(-20,120)
	forward(2)
	
	circle(-65,65)
	left(130)
	
	circle(65,80)
	right(66)
	circle(350,10)
	
	left(2)
	circle(300,6)
	left(5)
	circle(300,10)
	
	left(160)
	circle(-80,35)
	circle(-5,60)
	circle(-80,25)
	circle(-80,25)
	circle(-80,15)
	circle(195,47)
	left(125)
	
	circle(-400,12)
	right(35)
	circle(-83,90)
	right(20)
	circle(-200,25)
	circle(240,20)
	
	left(157)
	forward(185)
	right(15)
	circle(405,22)
	
	right(36)
	circle(285,15)
	circle(80,25)
	circle(50,28)
	left(115)
	circle(-145,20)
	circle(-10,30)
	right(40)
	circle(-100,60)
	circle(-255,32)
	left(160)
	circle(250,35)
	
	right(155)
	circle(-666,22)
	
	left(150)
	circle(380,35)
	
	right(166)
	circle(-660,15)
	circle(-500,14)
	end_fill()
	penup()

def del_1_nofill():

	fillcolor('white')
	pensize(pen10)
	pendown()
	begin_fill()
	circle(800,30)
	right(130)
	forward(340)
	right(128.7)
	circle(800,29.5)
	end_fill()
	penup()
	
# øyne, usikker på om disse skal være i samme funksjon.'
def start_3():
	home()
	goto(220,375)           
	pendown()
	right(55)
	
def del_3_fill():
	pendown()
	begin_fill()
	circle(-640,35)
	circle(-250,22)
	circle(20,120)
	forward(2)
	
	circle(65,65)
	right(130)
	
	circle(-65,80)
	left(66)
	circle(-350,10)
	
	right(2)
	circle(-300,6)
	right(5)
	circle(-300,10)
	
	right(160)
	circle(80,35)
	circle(5,60)
	circle(80,25)
	circle(80,25)
	circle(80,15)
	circle(-195,47)
	right(125)

	circle(400,12)
	left(35)
	circle(83,90)
	left(20)
	circle(200,25)
	circle(-240,20)
	
	right(157)
	forward(185)
	
	left(15)
	circle(-405,22)
	left(36)
	circle(-285,15)
	circle(-80,25)
	circle(-50,28)
	right(115)
	
	circle(145,20)
	circle(10,30)
	
	left(40)
	
	circle(100,60)
	circle(255,32)
	
	right(160)
	circle(-250,35)
	
	left(155)
	circle(666,22)
	
	right(150)
	circle(-380,35)
	
	left(166)
	circle(660,15)
	circle(500,14)
	
	end_fill()
	penup()
	
def øyne():
	fillcolor('white')
	
	# Øyne 1	
	#possisjon.
	penup()
	home()
	goto(-43,-165)
	right(180)
	forward(40)
	
	#tegne
	pendown()
	begin_fill()
	
	pensize(pen10)
	circle(-30,45)
	circle(100,45)
	circle(175,25)
	circle(80,5)
	circle(10,60)
	circle(10,60)
	circle(135,10)
	circle(200,45)
	
	end_fill()
	penup()
	home()
	
	# Øyne 2
	goto(43,-165)
	forward(40)
	
	pendown()
	begin_fill()
	
	pensize(pen10)
	circle(30,45)
	circle(-100,45)
	circle(-175,25)
	circle(-80,5)
	circle(-10,60)
	circle(-10,60)
	circle(-135,10)
	circle(-200,45)
	
	end_fill()
	penup()
	home()
	
	
speed(9)
start_1()
del_1_fill()
start_2()
del2()
start_3()
del_3_fill()
øyne()
ht()




##############################################

sleep(25)
