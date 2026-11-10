from pathlib import Path

caminhoDiario = Path("diario.txt")

# Escreve o DIA 1 (com \n no final para organizar a próxima linha)
with open('diario.txt', 'w', encoding="utf-8") as diary:
   diary.write("DIA 1 - Iniciando aula de arquivos!\n")

print("Escrito com sucesso!")

# Adiciona o DIA 2 usando o modo 'a'
with open(caminhoDiario, 'a', encoding="utf-8") as diary:
    diary.write("DIA 2 - Realizando atividade\n")

print("\n--- Lendo o Diário ---")

# Lê e imprime todas as linhas corretamente dentro do loop
with open(caminhoDiario, 'r', encoding="utf-8") as diary:
     for linha in diary:
            conteudo = linha.strip()
            print(conteudo)  # <-- O print precisa estar aqui dentro!




