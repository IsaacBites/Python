# -*- coding: utf-8 -*-

a = input()
b = input()
c = input()

MaiorAB = (a + b + abs(a-b)) / 2

Maior = (MaiorAB + c + abs(MaiorAB-c)) / 2

print(f"{Maior:.0f}" ' eh o maior')