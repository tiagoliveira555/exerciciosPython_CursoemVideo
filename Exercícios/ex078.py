listanum = list()
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('=-' * 30)
print(f'O número maior foi {max(listanum)} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == max(listanum):
        print(f'{i}... ', end='')
print()
print(f'O número menor foi {min(listanum)} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == min(listanum):
        print(f'{i}... ', end='')
print()
