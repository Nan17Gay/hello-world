#Você foi contratado para criar um programa de calculo de média de notas escolares
#esse programa recebera duas notas e calculará a media
#1.Solicitar o input das notas númericas [int ou float]
nota1 = int(input("Insira o primeiro numero da nota : "))
nota2 = int(input("Insira o segundo numero da nota : "))
#2.Realizar o calculo de média = (nota1 + nota2)/2
media = (nota1 + nota2) // 2
print(media)
#3.Verificar se o aluno tiver nota >=5, então aprovado, senão reprovado, para isso vamos fazer uma comparação.
if media >= 5:
    print("Aprovado")
else:
    print("Reprovado")
