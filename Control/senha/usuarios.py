import os
import json

# Cria o caminho do arquivo senhas.json
# O ".." volta uma pasta para trás
ARQUIVO = os.path.join(os.path.dirname(__file__), "..", "senhas.json")

# Função responsável por carregar os usuários salvos
def carregar():

    # Verifica se o arquivo existe
    if not os.path.exists(ARQUIVO):
        return {}

    # Verifica se o arquivo está vazio
    if os.path.getsize(ARQUIVO) == 0:
        return {}

    # Abre o arquivo em modo leitura
    with open(ARQUIVO, "r") as f:

        # Lê os dados do JSON e transforma em dicionário
        return json.load(f)

# Função responsável por salvar os dados
def salvar(dados):

    # Abre o arquivo em modo escrita
    with open(ARQUIVO, "w") as f:

        # Salva os dados no arquivo JSON
        # indent=4 deixa o arquivo organizado
        json.dump(dados, f, indent=4)