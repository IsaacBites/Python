# -*- coding: utf-8 -*-

raio = float(input())

A = 3.14159 * (raio * raio)
res = f"{A:.4f}".replace(" ", "")
print('A=' + res)