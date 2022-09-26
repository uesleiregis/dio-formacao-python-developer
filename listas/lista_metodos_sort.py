

linguagens = ['python', 'js', 'c', 'java', 'cobol', 'java']

print(linguagens)
print()


# sort
# ordena o vetor

linguagens.sort() #

print(linguagens)

# --------------------------------------

linguagens = ['python', 'js', 'c', 'java', 'cobol', 'java']

# sort reverse
# ordena o vetor e inverte a ordem

linguagens.sort(reverse = True) #

print(linguagens)

# ---------------------------------------

linguagens = ['python', 'js', 'c', 'java', 'cobol', 'java']

# sort lambda (função anonima)
# ordena o vetor pelo tamanho da string 
# lambda x é cada elemento do vetor


linguagens.sort(key = lambda x: len(x)) #

print(linguagens)

# ---------------------------------------

linguagens = ['python', 'js', 'c', 'java', 'cobol', 'java']

# sort lambda e reverse
# ordena o vetor pelo tamanho de cada string da lista

linguagens.sort(key = lambda x: len(x), reverse = True) #

print(linguagens)