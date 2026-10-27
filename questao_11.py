nota = float(input("digite a nota do aluno: "))

if nota >= 7:
    print("aprovado")
elif nota <= 6.9 and nota >= 5:
    print("recuperação")
elif nota < 5:
    print("reprovado")