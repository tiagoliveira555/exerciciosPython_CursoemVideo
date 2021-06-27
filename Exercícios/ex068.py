from random import randint
print('=-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*10)
v = 0
while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('-'*30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-'*30)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
print('=-='*10)
print(f'GAMER OVER! Você venceu {v} vezes.')
