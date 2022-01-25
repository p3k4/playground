from time import *
from math import *
from turtle import *

## Tegne smurf!
# total bredde: 450px
#total høyde: 490px

# Tegnes i rekkefølge: venstre fot og bein, underliv, høyre bein, hale, mage, venstre arm, hode,
#lufe, høre arm.
#


#gå til start posisjon (venstre bein, underside)

#globale variabler

#Pen tykkelse
p_1 = 5
p_2 = 15
p_3 = 20

## Tegne venstre bein, underside.
pensize(10)


#venstre sko og mage.
def v_sko():
	penup()
	goto(-225,-250)
	left(180)
	pensize(p_1)
	pendown()
	circle(55,60)
	penup()
	goto(-225,-245)
	right(95)
	penup()
	
	# gå til start av mage.
	circle(-100,20)
	pendown()
	
	#tegne mage:
	circle(-80,60) #sirkel 1
	circle(-160,35) #sirkel 2
	
	
	# Snu og gå tilbake for å tegne overside av venstrebein
	right(180)
	circle(160,35) #sirkel 2
	circle(80,50) #sirkel 1
	
	#gå til start av venstre overbein.
	
	right(180)
	circle(-100,5)
	
	#vendtre overbein.
	circle(10,50)
	circle(50,15)
	circle(20,75)

	#plassering venstre sko, høyre side.
	left(20) # Litt rar, men ser greit nok ut så langt
	
	#tegne høyre side av inner-fot/sko
	circle(130,20)
	circle(130,20)
	circle(-80,10)
	circle(-30,90)
	circle(-130,10)
	
	#venstre side av venstre sko.	
	circle(-100,10)
	circle(-40,45)
	circle(-350,10)
	circle(-200,10)
	
	#top av venstre sko
	right(10)
	circle(-100,70)
	circle(-100,10)
	right(10)
	circle(-50,60)
	circle(-70,40)
	penup()
	
	#snu for å tegne venstre sko skygge.
	right(180)
	circle(70,40)
	circle(50,60)
	right(-10)
	circle(100,10)
	circle(100,70)
	right(-10)
	circle(200,10)
	circle(350,10)
	circle(40,45)
	circle(100,10)
	circle(130,2.5)
	
	#plassering for å tegne skygge, venstre sko.
	left(15) #plassering
	pendown()
	
	#tegne skygge, vendtre sko
	circle(25,100)
	circle(-125,45)
	circle(35,75)
	penup()


##flytte til bunn av sko. med v_sko2 funksjon. Dårlig design valg,, men for å fullføre skoen der jeg var.

def h_sko():
	
	#gå tilstart punkt
	penup()
	goto(-225,-250)
	right(190)
	
	# begynne å tegne underliv
	pendown()
	circle(400,8)
	circle(-30,110)
	
	#høyre fot / sko0
	circle(180,10)
	left(10)
	circle(160,5)
	left(10)
	circle(60,30)
	left(10)
	circle(60,30)
	circle(100,30)
	left(10)
	circle(200,40)
	left(10)
	circle(80,20)
	circle(60,90)
	
	circle(45,55)
	circle(-200,30) #høyre sko ferdig.
	penup()
	home()
	
	#gå til startposisjon.
	goto(-225,-250)
	right(22)
	circle(400,8)
	circle(-30,110)
	
	circle(180,10)
	left(10)
	circle(160,5)
	left(10)
	circle(60,30)
	left(10)
	left(140)
	
	#begynne å tegne skygge høyre sko.
	pendown()
	circle(-60,65)
	circle(80,20)
	left(5)
	circle(-650,5)
	circle(-40,90)
	circle(-40,30)
	circle(-95,35)
	penup()
	
	#første detalj
	goto(-87.72,-406.29)
	right(190)
	forward(40)
	left(45)
	pendown()
	circle(30,100)
	penup()
	
	goto(-87.72,-406.29)
	right(60)
	forward(40)
	right(90)
	pendown()
	circle(-15,100)
	penup()
	home()
	
	#gå til startposisjon.
	goto(-225,-260)
	forward(140)
	left(90)
	
	#tegne hofte til liv
	pendown()
	right(20)
	circle(35,85)
	
	right(69)
	circle(130,26)
	
	#plassering, start på hale.
	right(180)
	circle(-130,8)
	left(90)
	circle(-30,165)
	penup()
	
	# gå til hofte
	home()
	goto(-112.25,-158.54)
	left(100)
	
	#tegne arm 1
	pendown()
	circle(90,10)
	penup()
	left(75)
	pendown()
	forward(15)
	right(180)
	forward(145)
	right(60)
	circle(100,15)
	
	#detalj i hånd
	right(180)
	circle(-100,20)
	right(180)
	circle(100,20)
	circle(35,20)
	left(5)
	circle(40,20)
	left(5)
	circle(40,20)
	left(10)
	circle(25,30)
	left(5)
	forward(15)
	circle(40,20)
	left(5)
	circle(35,30)
	left(5)
	circle(35,20)
	left(5)
	forward(5)
	left(5)
	forward(5)
	
	left(5)
	circle(20,150) #første finger er done..! Phew..
	circle(10,48)
	
	#detaljer i første finger.. fan
	left(60)
	circle(-20,50)
	right(180)
	circle(20,75)
	right(180)
	circle(-20,85)
	right(180)
	circle(20,10)
	circle(-10,85)
	penup()
	
	#neste finger starter her.
	home()
	goto(75,-145)
	
	#tegne neste finger.
	pendown()
	right(60)
	circle(50,15)
	circle(10,30)
	left(36)
	circle(60,32)
	circle(20,55)

	circle(100,15)
	circle(15,60)
	penup()
	
	#ny finger
	goto(116.89,-119.82)
	right(250)
	pendown()
	circle(20,25)
	circle(15,15)
	left(80)
	circle(60,20)
	circle(15,60)
	circle(145,15)
	ht()
	
	############## (116.89,-119.82)

	
	sleep(25)
	

#kjør funksjoner..
v_sko()
h_sko()
sleep(25)











