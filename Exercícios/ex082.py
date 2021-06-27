lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    sair = str(input('Quer continar? [S/N] '))
    if sair in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('=-' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
