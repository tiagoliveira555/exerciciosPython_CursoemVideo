n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[32mPRIMEIRO\033[m número é maior!')
elif n1 < n2:
    print('O \033[32mSEGUNDO\033[m número é maior!')
else:
    print('Os dois valores são \033[32mIGUAIS\033[m!')
