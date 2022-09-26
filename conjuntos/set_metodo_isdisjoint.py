conjunto_a = {1, 2, 3, 4, 5, 6}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

c = conjunto_a.isdisjoint(conjunto_b) 
d = conjunto_b.isdisjoint(conjunto_c)

print(c) 
print(d)