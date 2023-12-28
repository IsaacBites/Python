hora1 = int(input())
min1 = int(input())
hora2 = int(input())
min2 = int(input())

if 0 <= hora1 <= 23 and 0 <= min1 <= 59 and 0 <= hora2 <= 23 and 0 <= min2 <= 59:
    total_minutos1 = hora1 * 60 + min1
    total_minutos2 = hora2 * 60 + min2

    if total_minutos1 == total_minutos2:
        print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    else:
        duracao_total_minutos = (total_minutos2 - total_minutos1 + 24 * 60) % (24 * 60)
        duracao_horas = duracao_total_minutos // 60
        duracao_minutos = duracao_total_minutos % 60
        print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
else:
    print('Inválido')

