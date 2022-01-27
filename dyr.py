
# Snakkeboble:
def valg():
	inp = input("Hvilke dyr skal vises? \n") # prompt
	inp2 = input("Hva skal " + inp + "en si? \n") #prompt
	boble_lengde = len(inp2) + 2 # + 2 fordi '<' og '>' tegnene skal også medregnes.

# Ascii art (ku):
	if inp == 'Ku':
		print('_' * boble_lengde) # antall tegn av '_'  = inp + 2
		print('<' + inp2 + '>') 	  # tekst-input
		print('-' * boble_lengde) # # antall tegn av '-'  = inp + 2
		
		#Ku, Ascii:
		print('^__^')
		print('(oo)\_______')
		print('(__)\       )')
		print('    ||----W |')
		print('    ||     ||')

# Ascii art (elg):
	if inp == "Elg":
		
		print('_' * boble_lengde) # antall tegn av '_'  = inp + 2
		print('<' + inp2 + '>') 	  # tekst-input
		print('-' * boble_lengde) # # antall tegn av '-'  = inp + 2
		
		#Elg, Ascii:
		elg = r"      \ /----------\\"
		print("\n",'(_\_(___)_/_)')
		print('     (o o)    ')
		print(elg) 
		print('       O||        ||~')   
		print('        ||------/@|| ')
		print('        ||        || ')    
		print('        ^^        ^^ ') 
	if inp == 'Elefant':
	
		print('_' * boble_lengde) # antall tegn av '_'  = inp + 2
		print('<' + inp2 + '>') 	  # tekst-input
		print('-' * boble_lengde) # # antall tegn av '-'  = inp + 2
		
		#Elefant, Ascii:
		ele= r'  /=\""/=\  '
		print(ele)
		elf2= r' (=(0_0 |=)__   '
		print(elf2)
		elf3 =  r'  \_\ _/_/   )'
		print(elf3)
		elf4 = r"    /_/   _  /\ " 
		print(elf4)
		elf5 = r"    |/ |\ || |   "
		print(elf5)
		print("        ~ ~  ~")
		
#                                 |\    /|
#                             ___| \,,/_/
#                          ---__/ \/    \
#                         __--/     (D)  \
#                         _ -/    (_      \
#                        // /       \_ /  -\
#   __-------_____--___--/           / \_ O o)
#  /                                 /   \__/     - Look at my horse, my horse is amazing!
# /                                 /
#||          )                   \_/\
#||         /              _      /  |
#| |      /--______      ___\    /\  :
#| /   __-  - _/   ------    |  |   \ \
# |   -  -   /                | |     \ )
# |  |   -  |                 | )     | |
#  | |    | |                 | |    | |
#  | |    < |                 | |   |_/
#  < |    /__\                <  \
#  /__\                       /___\
	
valg()
