from pathlib import Path
from datetime import datetime

# Define o caminho do arquivo usando pathlib
caminho_arquivo = Path("dados.txt")

# Pega a data e hora atual para registrar no log
data_hora_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
nova_mensagem = f"[{data_hora_atual}] - Execução realizada com sucesso!\n"

# Abrindo com o modo 'a' (Append)
# O encoding="utf-8" garante que os caracteres especiais saiam certinhos
with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
    arquivo.write(nova_mensagem)

print("Nova linha adicionada ao arquivo com sucesso!")