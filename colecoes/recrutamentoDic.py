contador = 0
lista = []

while contador < 5:
    candidato = {}

    nomeCandidato = input("Digite o nome do candidato: ")
    candidato["nome"] = nomeCandidato

    idadeCandidato = int(input("Digite a idade do candidato: "))
    candidato["idade"] = idadeCandidato

    
    telefoneCandidato = input("Digite o telefone do candidato: ")
    candidato["telefone"] = telefoneCandidato

    emailCandidato = input("Digite o email do candidato: ")
    candidato["email"] = emailCandidato

    formacaoCandidato = input("Digite a formação do candidato: ")
    candidato["formação"] = formacaoCandidato

    lista.append(candidato)
    contador += 1

for candidato in lista:
    print(
        f"Nome: {candidato['nome']} | "
        f"Idade: {candidato['idade']} | "
        f"Telefone: {candidato['telefone']} | "
        f"Email: {candidato['email']} | "
        f"Formação: {candidato['formação']}"
    )




