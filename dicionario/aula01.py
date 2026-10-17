# Definindo dados com dicionario
dados = {'nome': "Valim", "idade" : 21}

# adicionando dado
dados["sexo"] = "M"

#deletando um dado
del dados["idade"]

# chamando dicionario
print(dados)

# keys == nomenclstura dos valores .. é o que está na primeira aspas
# value == nome atribuido .. é o que está na segunda aspas
# Item == a junção do value e o key 
filme = {
"titulo":"vingadores", # a junção destes key e value é um item
"ano":"2024",
"defnicao":"bom"
}

# repetiçao descrevendo os itens
for k, v in filme.items():
    print(f'{k} é {v}')
