# parametros nomeados e não nomeados

# o que vem antes da barra(/) é obrigatoriamente posicional
# o que vem depois do * é obrigatoriamente nomeado
# e o meio é opcional (marca)

def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-123", marca ="Fiat", motor = "1.0", combustivel="Gasolina")