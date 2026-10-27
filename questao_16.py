escudo_ativo = bool(input("voce tem escudo? (s/n): ") == True)
dano_base = 20

if escudo_ativo == True:
    print("recebeu 4 de dano")
else:
    print("recebeu 20 de dano")