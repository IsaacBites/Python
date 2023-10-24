texto = input("Digite uma palavra: ")
vogais = 0
texto = texto.lower()

for caractere in texto:
    if (caractere == 'a') or (caractere == 'e') or (caractere == 'i') or (caractere == 'o') or (caractere == 'u'):
        vogais+=1

print(vogais)
