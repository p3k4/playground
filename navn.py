from math import *
from time import *
from turtle import *

#Start-setup
shape('turtle')
pensize(20)

##Skrive navnet mitt:
# Bokstav, stor "P"
left(90) 	
forward(80) 	
right(90)	
circle(50,180)	
left(90) 	
forward(100)	

# Returnere til startpunkt
home()
penup()

# Gå til neste startpunkt
forward(50)
left(90)
forward(25)
right(90)

#begynner å tegne "e"
pendown()	
forward(25)	
circle(20, 270)	
forward(25)
circle(20,120)
right(30)
penup()

# Gå til neste startpunkt
forward(30)
left(90)

# tegne stor "R"
pendown()
forward(50)
circle(-20)
right(180)
forward(10)
left(30)
forward(50)
left(60)
penup()

#Gå til neste startpunkt
forward(200)
left(90)

#tegne stor "C"
forward(100)
left(90)
pendown()
circle(50,180)
penup()

#Gå til neste start punkt.
forward(25)
left(90)

# Tegne h
pendown()
forward(80)
right(180)
forward(40)
left(90)
circle(-25,90)
forward(20)
penup()

#Gå til neste startpunkt
left(90)
forward(25)
left(90)

# Tegne stor R
pendown()
forward(50)
circle(-20)
right(180)
forward(10)
left(30)
forward(50)
left(60)
penup()

#Gå til neste startpunkt
forward(50)
left(90)

#tegne i
pendown()
forward(60)
penup()

#prikken over "i"
forward(20)
right(30)
forward(10)
pendown()
circle(5)
penup()
left(210)
forward(80)

#nytt startpunkt
left(90)
forward(25)

#tegne s
pendown()
forward(10)
circle(15,180)
circle(-15,180)
forward(10)
penup()

#gå til neste startpunkt
forward(20)

#tegne "t"
pendown()
forward(24)
right(180)
forward(12)
right(90)
forward(20)
right(180)
forward(60)
circle(10,180)
penup()

#nytt startpunkt
right(180)
forward(20)
left(90)
forward(25)
left(90)

#tegne "i"
pendown()
forward(60)
penup()

#prikken over "i"
forward(20)
right(30)
forward(10)
pendown()
circle(5)
penup()
left(210)
forward(80)

#nytt startpunkt
left(90)
forward(60)
left(90)
forward(30)

#tegne "a"
pendown()
circle(25,180)
forward(10)
circle(25,160)
forward(20)
right(160)
forward(40)
penup()

#ny startposisjon
left(90)
forward(30)
left(90)

#tegne n
pendown()
forward(60)
right(150)
forward(80)
left(150)
forward(80)
sleep(10)
