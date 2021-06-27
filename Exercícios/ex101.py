def voto(ano):
    from datetime import datetime
    ano = datetime.now().year - ano
    if ano < 16:
        return f'Com {ano} anos: NÃO VOTA.'
    elif 16 <= ano < 18 or ano > 70:
        return f'Com {ano} anos: VOTO OPCIONAL.'
    else:
        return f'Com {ano} anos: VOTO OBRIGATÓRIO.'


print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
