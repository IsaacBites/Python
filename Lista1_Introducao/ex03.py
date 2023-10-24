palavra = input("Digite uma palavra ou frase: ")

palavra = palavra.replace(" ", "").lower()   #Tirando os espaços em branco e convertendo as letras para minúsculas


if palavra == palavra[::-1]:    #Invertendo a palavra e comparando as duas
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
