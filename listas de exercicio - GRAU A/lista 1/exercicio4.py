# 4. Como poderíamos tornar o programa acima mais genérico, de maneira que pudéssemos registrar qualquer questão objetiva com 5 alternativas?

pergunta = "Qual é o verdadeiro nome do super-herói Batman?"

A = "A) Bruce Wayne"
B = "B) Clark Kent"
C = "C) Peter Parker"
D = "D) Tony Stark"
E = "E) Steve Rogers"

alternativas = [A, B, C, D, E]

print(pergunta)

for i in (alternativas):
    print(i)