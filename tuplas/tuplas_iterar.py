frutas = ("laranja", "pera", "uva",)

for fruta in frutas:
    print(fruta)

carros = ("gol", "celta", "palio")

for carro in carros:
    print(carro)

print()

# usando enumerate

for indice, carro in enumerate(carros):
    print(f"Índice: {indice}, Modelo do carro: {carro}")