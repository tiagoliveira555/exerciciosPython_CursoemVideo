dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
diasrodados = dias * 60
kmrodados = km * 0.15
total = diasrodados + kmrodados
print('Você ficou {} dias com o carro, então irá pagar R${:.2f}.'.format(dias, diasrodados))
print('Como você rodou {}Km, irá pagar R${:.2f}.'.format(km, kmrodados))
print('No total você irá pagar R${:.2f}.'.format(total))
