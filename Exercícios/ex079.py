numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
print('=-' * 30)
numeros.sort()
print(f'Você digitou os valores {sorted(numeros)}.')
