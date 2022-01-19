from time import *
from turtle import *

#Variabler
pensize(50)
inn = textinput("Velg sirkel","Velg hvilken type sirkel som skal tegnes (\"Orange fylt\", \"Blå linje\" eller \"Lilla fylt\").")

# sjekker input, minner meg om "switch" fra javascript enn så lenge.
if inn == ('Orange fylt'):
	color('Orange')
	begin_fill()	#betingelser må skrives med innrykk!
	circle(100)	#betingelser må skrives med innrykk!
	end_fill()	#betingelser må skrives med innrykk!

elif inn == ('Blå linje'):
	color('blue')
	circle(100)	

elif inn ==('Lilla fylt'):
	color('indigo')
	begin_fill()
	circle(100)
	end_fill()	
else:			
	exit() #sirkelen tegnes ikke
sleep(3)

## if-elif-else fakta:
# Det er maksimalt 1 "if" og "else" setning for hver betingelse. 
# Vi kan derimot ha så mange "elif" vi behøver, evt. ønsker oss til jul, bursdag eller andre merkedager!
# Funfact: elif er boolean og dermed også en betingelse!
# "else" er ikke et krav for å få koden til å kjøre. Husk derimot på innrykk og kolon i syntax!
