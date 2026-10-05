# usuário digitará o nome e o bairro de
# dez pessoas. O programa exibirá o nome e bairro das pessoas em ordem
# alfabética.
cadastro = []
for i in range (0,4):
    nome = str(input("digite o nome: \n"))
    bairro = str(input("digite o bairro: \n"))
    cadastro[i] = [nome, bairro]

# ordenar pelo nomne
    cadastro.sort()

# ordenar pelo bairro
    cadastro.sort(key=lambda x: x[1])

print("a lista esta desta forma: \n" + cadastro)

