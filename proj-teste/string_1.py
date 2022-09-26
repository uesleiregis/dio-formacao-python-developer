# maiúsculas e minúsculas
nome = 'UésLei'
print(nome.upper())
print(nome.lower())
print(nome.title())

# strip

nome2 = "          Espaços em Branco    "

print(nome2)
print(nome2.strip()+'.')
print(nome2.lstrip()+'.')
print(nome2.rstrip()+'.')

menu = 'Python'

print("###"+menu+"###")
print(menu.center(14))
print('P-y-t-h-o-n')
print('-'.join('Python'))

for letra in menu:
    print(letra, end="-")
print()
