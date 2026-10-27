pontos = int(input("quantos pontos voce tem?: "))
nivel = 1
vida = 100

if pontos > 1000:
    nivel += 1
    vida += 100
    print(f"parabens, voce subiu para o nivel {nivel} e sua vida aumentou para {vida}!")