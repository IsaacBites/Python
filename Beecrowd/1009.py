# -*- coding: utf-8 -*-

nome = input()
salario = float(input())
montante = float(input())

total = salario + (montante * 0.15)

print('TOTAL = R$ ' f"{total:.2f}")