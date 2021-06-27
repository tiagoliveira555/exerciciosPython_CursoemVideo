def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


print('Controle de Terrenos')
print('-' * 20)
la = float(input('LARGURA (m): '))
co = float(input('COMPRIMENTO (m): '))
área(la, co)
