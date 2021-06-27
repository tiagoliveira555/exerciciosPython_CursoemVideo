dis = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(dis))
# valor = dis * 0.50 if dis <= 200 else dis * 0.45
if dis <= 200:
    valor = dis * 0.50
else:
    valor = dis * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(valor))
