texto = 'Uéslei Regis da Costa Marques'
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')

print()