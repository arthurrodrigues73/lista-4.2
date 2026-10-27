tem_chave = bool(input("voce tem a chave? (s/n): ") == True )
distancia_porta = int(input("qual a distancia da porta?:"))

if tem_chave == True and distancia_porta < 2:
    print("porta aberta")
else:
    print("porta trancada")