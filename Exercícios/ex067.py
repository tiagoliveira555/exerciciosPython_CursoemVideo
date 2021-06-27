print('-'*10, 'TABUADA', '-'*10)
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 29)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')
    print('-'*29)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
