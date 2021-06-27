from random import randint
from time import sleep
sort = []
temp = []
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
jog = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= jog:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont == 6:
            break
    temp.sort()
    sort.append(temp[:])
    temp.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {jog} JOGOS', '=-' * 3)
for i, l in enumerate(sort):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 4, '< BOA SORTE! >', '=-' * 4)
