s = t = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    s += 1
    t += n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(s, t))
