lista = [1, "Python", [40,30,20]]

l2 = lista.copy()

print(lista) #[1, 'Python', [40, 30, 20]]

l2[0] = 2

print(l2)
print(lista)

print(id(l2), id(lista))

print(l2[0])