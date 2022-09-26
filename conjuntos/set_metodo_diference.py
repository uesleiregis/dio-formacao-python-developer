# tudo que tem num conjunto que não tem no outro

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

c = conjunto_a.difference(conjunto_b)
d = conjunto_b.difference(conjunto_a)

print(c)
print(d)