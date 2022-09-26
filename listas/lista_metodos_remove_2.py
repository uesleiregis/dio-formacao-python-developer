linguagens = ['python', 'js', 'c', 'java', 'cobol', 'java', 'java']

palavra = str(input(f"Informe a palavra para remover de \n{linguagens}\n"))

cont = 0
while(linguagens.count(palavra) > 0):
    cont += 1
    linguagens.remove(palavra)

print(f'Novo vetor: \n{linguagens}\nPalavras removidas: {cont}')