from turtle import *
from time import *
# Jeg har tidligere lært at dette kalles 'casting', ved å konvertere datatyper til andre datyper.
# Det fungerer også i python og har mange bruksområder!
#--------------------------------------------------------------------------------------------------#
#variabler
tall = 4
print(tall) #utskrift av verdien til "tall"

des = float(tall) # casting til float
print (des) #utskrift av verdien til "tall"

hel = int(tall) # casting til int
print (hel) #utskrift av verdien til "tall"

streng = str(tall) # casting til string
print(streng) #utskrift av verdien til "tall"

#--------------------------------------------------------------------------------------------------#
#user input blir konvertert til int slik at funksjonen color() kan tolke verdien.
rød = int(numinput("Design", "Velg intensitet av rød"))
grønn = int(numinput("Design", "Velg intensitet av grønn"))
blå = int(numinput("Design", "Velg intensitet av blå"))

colormode(255) #farge-spekteret skal gå fra 0 til 255
color(rød, grønn, blå) # Tar imot input fra variablene som hånterer brukerinput
pensize(50)
circle(100) # Tegner en sirkel for å teste koden

# Venter før programmet lukkes
sleep(5)

