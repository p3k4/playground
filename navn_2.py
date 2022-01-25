from turtle import *
from math import *
from time import *

#setup og startposisjon
penup()
goto(-500,0)
pensize(5)
## Skrive navn med fylte bokstaver

#Ny startpositsjon
forward(30)
penup()
pendown()

#Fyll P
fillcolor('Purple')
begin_fill()
forward(30)
circle(45,180)
forward(65)
left(90)
forward(200)
left(90)
forward(35)
left(90)
forward(110)
end_fill()

#Sirkel i "P"
penup()
forward(30)
right(90)
pendown()
fillcolor('white')
begin_fill()
forward(30)
circle(15,180)
forward(30)
left(90)
forward(30)
end_fill()
penup()

#ny startposisjon
forward(140)
left(90)
forward(50)
left(90)
right(90)

#Fyll "e"
fillcolor('Red')
begin_fill()

pendown()
circle(40,90)
left(90)
forward(30)
left(90)
circle(-10,180)
forward(10)
right(90)
forward(50)
left(90)
circle(40,180)
forward(10)
circle(40,90)
end_fill()
penup()

#sirkel i "e"
left(90)
forward(60)
right(90)

#fyll og form i sirkel "e"
pendown()
fillcolor('white')
begin_fill()
forward(10)
left(90)
circle(10,180)
left(90)
forward(10)
end_fill()
penup()

#Ny startposisjon
right(90)
forward(60)
left(90)
forward(50)
left(90)

#liten "r"
pendown()
fillcolor('Orange')
begin_fill()
forward(80)# bokstavens høyde
right(90)
forward(30)
right(90)
forward(20)
left(180)
circle(-20,90)
forward(15)
right(90)
forward(30)
right(90)
circle(35,90)
forward(15)
right(90)
forward(30)
end_fill()
penup()

#ny start posisjon
right(180)
forward(200)
left(90)

#Liten "c"
pendown()
fillcolor('Light Blue')
begin_fill()
forward(30)
left(90)
forward(15)
circle(-20,180)
forward(15)
left(90)
forward(30)
left(90)
forward(15)
circle(50,180)
forward(15)
end_fill()
penup()

#Ny start posisjon
forward(20)

#bokstav h
pendown()
fillcolor('Green')
begin_fill()
forward(30) #bredde på beina
left(90)
forward(35) # høyde på beina
right(90)
forward(20)
right(90)
forward(35) #høyde på beina
left(90)
forward(35) #bein til høyre
left(90)
forward(100) #høyde på bokstaven
left(90)
forward(35)
left(90)
forward(35)
right(90)
forward(20)
right(90)
forward(35)
left(90)
forward(35)
left(90)
forward(100)
left(90)
forward(10)
end_fill()
penup()

#Ny startposisjon
forward(90)
left(90)
pendown()

fillcolor('Pink')
begin_fill()
forward(80)# bokstavens høyde
right(90)
forward(30)
right(90)
forward(20)
left(180)
circle(-20,90)
forward(15)
right(90)
forward(30)
right(90)
circle(35,90)
forward(15)
right(90)
forward(30)
end_fill()
penup()

# Ny startposisjon
right(180)
forward(80)
left(90)
pendown()

## liten "i"
fillcolor('Blue')
begin_fill() #Fyll i både bokstav og sirkel over "i"
forward(80)
right(90)
forward(30)
left(90)
penup()


#sirkel over "i"
forward(25)
pendown()
circle(15)
penup()

# fullføre bokstaven
left(180)
forward(25)
pendown()
left(90)
right(90)
forward(80)
right(90)
forward(30)
end_fill() #Fyll i både bokstav og sirkel over "i"
penup()

#Ny startposisjon
right(180)
forward(50) #avstand til neste bokstav

#tegne "s"
pendown()
fillcolor('Yellow')
begin_fill()
forward(60) #bunn
circle(10,90)	#første 90 sirkel
forward(30) # høyde på første
circle(10,90)	

#inni
forward(30)
circle(-5,180)
forward(35)

# fullføre "s"
circle(5,90)
forward(20)
circle(10,90)
forward(60)
circle(10,90)
forward(45)
circle(5,90)
forward(35)
circle(-5,180)
forward(35)
circle(5,90)
forward(15)
circle(5,90)
forward(60)
end_fill()
penup()

#Nytt startpunkt
forward(100)
left(90)
forward(30)

## tegne "t"

#første halvdel
pendown()
fillcolor('Grey')
begin_fill()
left(90)
forward(25)
left(90)
circle(-5,180)
forward(60)
right(90)
forward(15)
left(90)
forward(15)
left(90)
forward(15)
right(90)
forward(20)
left(90)
forward(30)

#andre halvdel
left(90)
forward(20)
right(90)
forward(15)
left(90)
forward(15)
left(90)
forward(15)
right(90)
forward(60)
circle(35,180)
end_fill()
penup()

#ny startposisjon
right(180)
forward(30)
left(90)
forward(10)
left(90)

#liten "i"
pendown()
fillcolor('#3c6e91')
begin_fill() #Fyll i både bokstav og sirkel over "i"
forward(80)
right(90)
forward(30)
left(90)
penup()

#sirkel over "i"
forward(25)
pendown()
circle(15)
penup()

# fullføre bokstaven
left(180)
forward(25)
pendown()
left(90)
right(90)
forward(80)
right(90)
forward(30)
end_fill() #Fyll i både bokstav og sirkel over "i"
penup()

#ny startposisjon
right(180)
forward(130) #avstand til neste bokstav
left(90)
forward(30)
left(180) #startgrad

##tegne liten "a"

# start detailj
pendown()
fillcolor("#ffa60b")
begin_fill()
circle(-2,180)

#strek høyre side
forward(60)
left(90)
forward(20)
left(90)
forward(20)
left(180)

# sirkel-del 1
circle(20,90)
forward(20)
circle(20,90)

# sirkel-del 2
forward(40)
circle(28,90)
forward(15)

#sirkel-del 3
circle(20,90)
right(180)

#siste del av detaljen
circle(20,90)
forward(5)
circle(10,90)
forward(20)

left(90)
forward(13)
penup()
end_fill()

#sirkel i "a"
forward(40)
pendown()
fillcolor('white')
begin_fill()
forward(10)
circle(-10,90)
forward(10)
circle(-10,90)
forward(5)
circle(-10,90)
forward(10)
circle(-10,90)
forward(10)
end_fill()
penup()

#ny startposisjon
left(90)
forward(30)
left(90)
forward(80) #avstand til ny bokstav
left(90)

#tegne "n"
pendown()
fillcolor("#b975fc")
begin_fill()

#første strek opp og til høyre
forward(90)
right(90)
forward(35)
right(90)
forward(20)
right(180)

#halv-sirkel
circle(-20,180)
forward(70) #strek til høyre
right(90)

#nederste del av linje 2 
forward(30) 
right(90)
forward(40) #høyde
circle(5,180) #sirkel
forward(40)	#ned
right(90)
forward(35)
end_fill()

print("done")
sleep(20) #sleep



































