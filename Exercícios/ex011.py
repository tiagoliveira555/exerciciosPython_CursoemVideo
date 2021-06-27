larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area:.2f}m².')
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')
