def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        nu = str(input(msg))
        if nu.isnumeric():
            valor = int(nu)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
