def somar(a,b):
    return a+b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"o resultado da operação é  {resultado}\n")

# def exibir_resultado(a, b, funcao):
#     resultado = funcao(a, b)
#     print(f"o resultado da operação {a} + {b} = {resultado}\n")

exibir_resultado(10,10, subtrair) # passo somente o nome da função 
exibir_resultado(10,10, somar) # passo somente o nome da função 

op = somar

print(op(1,23))