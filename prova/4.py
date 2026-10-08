# a. Desenvolva um sistema de console para auditar o consumo elétrico de maquinários em uma
# linha de produção industrial. O sistema deve monitorar 5 máquinas utilizando vetores
# unidimensionais.
indiceMaior = 0
maquinaLista = []
codigoNumerico = []
listaConsumo = []
media = 0
contador = 0

# O programa deve preencher duas listas paralelas de tamanho fixo (5
# posições)

# uma contendo o código numérico de identificação de cada
# máquina
for i in range (5):
    numMaq = input("Digite a maquina: \n")
    maquinaLista.append(numMaq)



# e outra contendo o respectivo consumo registrado em quilowatt-
# hora (kWh).
for j in range (5):
    consumo = float(input("Digite o consumo da maquina: \n"))
    # Para cada máquina, o sistema deve validar a entrada do consumo através de
    # um laço while, garantindo que o valor informado em kWh seja estritamente
    # maior que zero antes de passar para a máquina seguinte.
    while consumo <= 0:
        consumo = float(input("numero negado!: \nDigite novamente\n"))
    listaConsumo.append(consumo)


# Solicite ao operador o valor do "Teto Operacional de Consumo" (número real
# único para a verificação de toda a linha industrial).
tetoOp = int(input("Digite um teto operacional:\n"))
#varredura

# Realize uma varredura nas estruturas e identifique:

# a. Quais máquinas ultrapassaram o teto operacional, exibindo seu
# código e o consumo registrado;
for k in range (5):
    if listaConsumo[k] > tetoOp:
        print(f"maquina código: {maquinaLista[k]}, consumo: {listaConsumo[k]} Acima do teto Operacional")
        contador += 1
        # b. O código e o consumo da máquina com o maior consumo absoluto da
# planta;
    if listaConsumo[k] > listaConsumo[indiceMaior]:
        indiceMaior = k

# c. A média aritmética de consumo de todas as 5 máquinas.
soma = 0
for l in range (5): 
    soma += listaConsumo[l]
media = soma / 5

# Caso nenhuma máquina tenha ultrapassado o teto operacional, o programa
# deve exibir a mensagem: "Operação Dentro dos Parâmetros de Eficiência".
if contador == 0:
    print("Operação Dentro dos Parâmetros de Eficiência")









