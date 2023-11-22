# -*- coding: utf-8 -*-

codigo = int(input())
quant = int(input())

precos = {
    1: 4.0,
    2: 4.5,
    3: 5.0,
    4: 2.0,
    5: 1.5
}	


if codigo in precos:
    total = precos[codigo] * quant
    print('Total: R$ 'f"{total:.2f}")
else:
    print("Código inválido")
