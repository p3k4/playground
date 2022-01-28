
# Snakkeboble:
def valg():
	inp = input("Hvilke dyr skal vises? \n") # prompt
	inp2 = input("Hva skal " + inp + " si?" "\n") #prompt
	boble_lengde = len(inp2) + 2 # + 2 fordi '<' og '>' tegnene skal også medregnes.

# Ascii art (ku):
	if inp == 'Ku':
		print('_' * boble_lengde)
		print('<Mø! ' + inp2 + '>')
		print('-' * boble_lengde) 
		boble_lengde = len(inp2) + 2 
		#Ku, Ascii:
		print('^__^')
		print('(oo)\_______')
		print('(__)\       )')
		print('    ||----W |')
		print('    ||     ||')

# Ascii art (elg):
	if inp == "Elg":
		
		print('_' * boble_lengde)
		print('<' + inp2 + '>')
		print('-' * boble_lengde)
		boble_lengde = len(inp2) + 2
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
		boble_lengde = len(inp2) + 2
		print('_' * boble_lengde)
		print('<' + inp2 + '>') 
		print('-' * boble_lengde)
		
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

	if inp == 'Fisk':
		boble_lengde = len(inp2) + 27
		print('_' * boble_lengde)
		print('<blub-blub.. ' + inp2 + '..blub-blub..>')
		print('-' * boble_lengde)
		
		#Fisk, Ascii:
		print(r"       o                 o")
		print(r"                  o")
		print(r"         o   ______      o")
		print(r"           _/  (   \_")
		print(r" _       _/  (       \_  O")
		print(r"| \_   _/  (   (    0  \"")
		print(r"|== \_/  (   (          |")
		print(r"|=== _ (   (   (        |")
		print(r"|==_/ \_ (   (          |")
		print(r"|_/     \_ (   (    \__/")
		print(r"           \_ (      _/")
		print(r"            |___/")
		print(r"            /__/")
		
	if inp == 'Edderkopp':
		boble_lengde = len(inp2) + 33
		print('_' * boble_lengde)
		print('<Tik-tik..ssh ' + inp2 + '..ssh, tisk-tisk..>') 
		print('-' * boble_lengde)

		#edderkopp ascii:
		
		print(r"               (")
		print(r"               )")
		print(r"              (")
		print(r'        /\  .-"""-.  /\"')
		print(r"       //\\/  ,,,  \//\\")
		print(r"       |/\| ,;;;;;, |/\|")
		print(r'       //\\\;-"""-;///\\')
		print(r"      //  \/   .   \/  \\")
		print(r"     (| ,-_| \ | / |_-, |)")
		print(r"       //`__\.-.-./__`\\")
		print(r"      // /.-(() ())-.\ \\")
		print(r"     (\ |)   '---'   (| /)")
		print(r"       ` (|           |) `")
		print(r"         \)           (/")
	
	if inp == 'Kanin':
		boble_lengde = len(inp2) + 2 # + 2 fordi '<' og '>' tegnene skal også medregnes.
		print('_' * boble_lengde) # antall tegn av '_'  = inp + 2
		print('<' + inp2 + '>') 	  # tekst-input
		print('-' * boble_lengde) # # antall tegn av '-'  = inp + 2
		
		#Kanin, ascii:
		print(r'     / \"')
		print(r'    / _ \"')
		print(r"   | / \ |")
		print(r"   ||   || _______")
		print(r'   ||   || |\     \"')
		print(r'   ||   || ||\     \"')
		print(r"   ||   || || \    |")
		print(r"   ||   || ||  \__/")
		print(r"   ||   || ||   ||")
		print(r"    \\_/ \_/ \_//")
		print(r'   /   _     _   \"')
		print(r'  /               \"')
		print(r"  |    O     O    |")
		print(r"  |   \  ___  /   |    ")
		print(r' /     \ \_/ /     \"')
		print(r'/  -----  |  --\    \"')
		print(r"|     \__/|\__/ \   |")
		print(r"\       |_|_|       /")
		print(r" \_____       _____/")
		print(r"       \     /")
		print(r"       |     |	")

	print("Prøv et annet dyr..")
	valg()	
valg()
