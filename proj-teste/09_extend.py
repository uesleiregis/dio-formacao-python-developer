#minha_lista.extend()
#quando queremos adicionar listas inteiras na minha lista de uma vez (sem precisar usar o .append())

# linguagens = ["python", "js", "c"]

# print(linguagens) # ['python', 'js', 'c']

# linguagens.extend(['java', 'ccharp']) #['python', 'js', 'c', 'java', 'ccharp']

# print(linguagens) 


#sem extend - praticando
aprovados = ['gabriel', 'monica', 'thiago']
reprovados = ['hiago', 'elisangela', 'mikael']

todos_alunos = [aprovados, reprovados]
print(todos_alunos)

#com extend - praticando
aprovados_1 = aprovados.copy()
aprovados_1.extend(['lucas','amadeu'])

print(aprovados_1)
