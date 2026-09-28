
#Construa um programa onde o usuário digitará seis notas (números reais). O programa
#deve calcular a média dessas notas e, em seguida, exibir quantas e quais notas ficaram
#estritamente acima da média calculada.

notas = []

for i in range(0,6):
    nota = input(float("Digite sua nota"))
    notas.append(nota)

media = sum(notas) / len(notas)
