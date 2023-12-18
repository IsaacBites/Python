# -*- coding: utf-8 -*-

a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((a + b) * c) / 2
    print(f"area = {area:.1f}")