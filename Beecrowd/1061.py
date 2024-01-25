dia_inicio = input().split()
hora_inicio = input().split(" : ")
dia_fim = input().split()
hora_fim = input().split(" : ")

dia_inicio = int(dia_inicio[1])
hora_inicio = list(map(int, hora_inicio))
dia_fim = int(dia_fim[1])
hora_fim = list(map(int, hora_fim))

segundos_inicio = dia_inicio * 24 * 60 * 60 + hora_inicio[0] * 60 * 60 + hora_inicio[1] * 60 + hora_inicio[2]
segundos_fim = dia_fim * 24 * 60 * 60 + hora_fim[0] * 60 * 60 + hora_fim[1] * 60 + hora_fim[2]
diferenca_segundos = segundos_fim - segundos_inicio

dias = diferenca_segundos // (24 * 60 * 60)
diferenca_segundos %= (24 * 60 * 60)
horas = diferenca_segundos // (60 * 60)
diferenca_segundos %= (60 * 60)
minutos = diferenca_segundos // 60
segundos = diferenca_segundos % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
