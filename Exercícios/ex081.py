numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sair == 'N':
        break
print('=-' * 30)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
