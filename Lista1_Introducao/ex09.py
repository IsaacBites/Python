n = input('Digite ("c" para °C) ou ("f" para °F): ')


if n == 'c':
    celsius = int(input('Insira uma temperatura em °C: '))
    tot = (celsius * 9/5) +32
    print(tot)
elif n == 'f':
    f = int(input('Insita uma temperatura em °F: '))
    tot  = (f -32) * 5/9
    print(tot)
else:
    print('Letra inválida')