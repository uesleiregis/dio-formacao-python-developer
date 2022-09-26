# mostra a primeira ocorrência do elemento
linguagens = ['python', 'js', 'c', 'java', 'cobol', 'java', 'java']


# escolhendo a palavra a ser removida
remover = str(input(f"Informe a palavra do vetor {linguagens} para ser substituida: "))

substituir = str(input(f"Informe a palavra para substituir {remover} : "))

cont = 0
while(linguagens.count(remover) > 0):
    print(f"{substituir} substituida na posição {linguagens.index(remover)}")
    linguagens[linguagens.index(remover)]= substituir
    print(f"\nNovo vetor\n{linguagens}\n")
    
