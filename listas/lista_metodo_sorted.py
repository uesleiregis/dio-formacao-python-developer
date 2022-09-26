linguagem = ["python", "js", "c", "java", "csharp"]



print()
print(sorted(linguagem, key = lambda x: len(x)))
print()


# ------------------------------- 
linguagem = ["python", "js", "c", "java", "csharp"]

print()
print(sorted(linguagem, key=lambda x: len(x), reverse=True))
print()