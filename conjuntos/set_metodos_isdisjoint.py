# metodo isdisjoint python
# identifica se dois conjuntos são disjuntos.

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

a = conjunto_a.isdisjoint(conjunto_b)
b = conjunto_a.isdisjoint(conjunto_c)

print(a, b)
