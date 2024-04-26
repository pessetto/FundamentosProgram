# 3) Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

numero = float(input('Digite um número: '))

if numero >= 0:
    dobro = numero*2
    print("O dobro do número digitado é ", dobro)

else:
    triplo = numero*3
    print("O triplo do número digitado é", triplo)