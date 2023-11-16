# -*- coding: utf-8 -*-

dias_vida = int(input())

anos = dias_vida // 365
rest_anos = dias_vida % 365

meses = rest_anos // 30
rest_meses= rest_anos % 30

dias =  rest_meses // 1

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")