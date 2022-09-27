contatos = {"ueslei123@gmail.com": {"nome": "Uéslei", "telefone": "3333-2221"}}

print(contatos)
print()
resultado = contatos.pop("ueslei123@gmail.com")
print(contatos)
print(resultado)
resultado = contatos.pop("ueslei123@gmail.com", "não encontrado")

print(resultado)



