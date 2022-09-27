

    # Programa remove a palavra desejada do vetor



linguagens = ['python', 'js', 'c', 'java', 'cobol', 'java', 'java']


# escolhendo a palavra a ser removida
remover = str(input(f"Informe a palavra do vetor {linguagens} para ser removida: "))



cont = 0
while(linguagens.count(remover) > 0):
    print(f"{remover} substituida na posição {linguagens.index(remover)}")
    linguagens.pop(linguagens.index(remover))
    print(f"\nNovo vetor\n{linguagens}\n")