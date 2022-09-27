from itertools import count


contatos = {
    "guilherme@gmail.com": {'nome': 'Guilherme', 'telefone': '3334-1223'},
    "lucas@gmail.com": {'nome': 'lucas', 'telefone': '3334-1223'},
    "anae@gmail.com": {'nome': 'Ana', 'telefone': '3334-1223'},
    "zéerme@gmail.com": {'nome': 'Zé', 'telefone': '3334-1223'}
}


lista_chaves: list = contatos.keys()

print(lista_chaves)
#index = lista_chaves.index("guilherme@gmail.com")
# count = lista_chaves.count("guilherme@gmail.com")

resultado = "guilherme@gmail.com" in contatos
print(resultado)
resultado = "megui@gmail.com" in contatos
print(resultado)


resultado = 'idade' in contatos['guilherme@gmail.com']
print(resultado)
resultado = 'telefone' in contatos['guilherme@gmail.com']
print(resultado)