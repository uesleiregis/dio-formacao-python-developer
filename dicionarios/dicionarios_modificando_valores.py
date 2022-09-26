dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(f"""
{
dados["nome"],
dados["idade"],
dados["telefone"],
}
""")


dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(f"""
{
dados["nome"],
dados["idade"],
dados["telefone"],
}
""")