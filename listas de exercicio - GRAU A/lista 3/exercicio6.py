# 6) Brincadeira do PAR ou ÍMPAR. Pergunte para o usuário se ele aposta em PAR ou ÍMPAR. Depois disso, peça para ele digitar um número de 0 a 5 (como se fosse mostrar os dedos da mão. Sorteie um número de 0 a 5 e some com o que o usuário digitou. Se o usuário escolheu PAR e o valor da soma for par OU se ele escolheu ÍMPAR e o valor da soma é ímpar, diga que ele venceu. Senão, diga que o programa venceu

import random
usuario = input("Digite P para escolher par e I para impar: ")
numeroU = int(input('Digite um número de 0 a 5: '))

sorteio = random.randint(1,5)
print('Numero sorteado pela máquina: ', sorteio)

if usuario == 'P' and ((numeroU + sorteio)%2)==0:
    print('Você ganhou!')

elif usuario == 'I' and ((numeroU + sorteio)%3)==0:
    print('Você ganhou!')

else:
    print('O programa ganhou, tente novamente :(')