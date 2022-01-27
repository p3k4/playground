inp = input("Hva skal kua si? \n")
boble_lengde = len(inp) + 2 # + 2 fordi '<' og '>' tegnene skal også medregnes.

# Snakkeboble:
print('_' * boble_lengde) # antall tegn av '_'  = inp + 2
print('<' + inp + '>') 	  # tekst-input
print('-' * boble_lengde) # # antall tegn av '-'  = inp + 2

# Ascii art:
print('^__^')
print('(oo)\_______')
print('(__)\       )')
print('    ||----W |')
print('    ||     ||')
