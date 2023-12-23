hora1 = int(input())
hora2 = int(input())

if 0 <= hora1 <= 23 and 0 <= hora2 <= 23:
    if hora1 == hora2:
        result = hora2 - hora1
        print('O JOGO DUROU 24 HORAS(S)')
    else:
        result = (hora2 - hora1 + 24) % 24
        print(f"O JOGO DUROU {result} HORAS(S)")
else:
    print('Inválido')
