# -*- coding: utf-8 -*-

A = int(input())
B = int(input())
C = int(input())
D = int(input())

if((B > C) and (D > A) and (D+C > A+B) and (C > 0) and (D > 0) and (A %2==0)):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
