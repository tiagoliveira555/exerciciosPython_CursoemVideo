print('-'*40)
print('{: ^40}'.format('SUPER BARATÃO'))
print('-'*40)
total = cont = totmil = menor = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    total += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        barato = produto
        menor = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'Foram {cont} produtos no total, e curstará R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')
