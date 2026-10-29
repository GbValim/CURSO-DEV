# colocando um dicionário em uma lista



brasil = []

estado01 = {"nome" : "Rio de Janeiro",
             "sigla" : "RJ",
             }
estado02 = {"nome" : "São Paulo",
            "sigla" : "SP"}

# adicionando dicionario na lista
brasil.append(estado01)
brasil.append(estado02)

# chamando a chave da primeira posição
print(brasil[0]["sigla"])