# -*- coding: utf-8 -*-

num_func = int(input())
horas_trabalhadas = int(input())
val_hora = float(input())

salario = horas_trabalhadas * val_hora

print('NUMBER =', num_func)
print('SALARY = U$', f"{salario:.2f}")