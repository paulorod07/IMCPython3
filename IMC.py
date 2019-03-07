print('Bem Vindo ao calculador de médias!')

nome = (input('digite seu nome: '))

nota1 = float(input('digite sua primeira nota: '))
nota2 = float(input('digite sua segunda nota: '))
nota3 = float(input('digite sua terceira nota: '))
nota4 = float(input('digite sua quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 6:
    print(nome,'foi aprovado com média:',media)
if media < 4:
    print(nome,'foi reprovado com média:',media)
if media == 4:
    print(nome,'está em recuperação com média:',media)