nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

media = (nota1 * 2  + nota2 * 3 + nota3 * 4 + nota4) / 10


if media < 5.0:
    print('Media: 'f"{media:.1f}")
    print('Aluno reprovado.')

elif media < 7.0:
    while True:
        exame = float(input())
        mediafinal = (media + exame)/2
        if mediafinal >= 5.0:
            print('Media: 'f"{media:.1f}")
            print('Aluno em recuperação.')
            print('Nota do exame: 'f"{exame:.1f}")
            print('Aluno aprovado.')
            print('Media final: 'f"{mediafinal:.1f}")
        else:
            print('Nota do exame: 'f"{exame:.1f}")
            print('Aluno reprovado.')
            print('Media final: 'f"{mediafinal:.1f}")

else:
    print('Media: 'f"{media:.1f}")
    print('Aluno aprovado.')
