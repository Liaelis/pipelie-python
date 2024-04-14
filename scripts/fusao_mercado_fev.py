import json
import csv
from processamento_dados import Dados

path_json = '/'
path_csv = '/'
path_dados_combinados = '/'



# Leitura dos dados

dados_empresaA = Dados(path_json,'json')
dados_empresaB = Dados(path_csv, 'csv')
#print(dados_empresaA.dados)

print(dados_empresaA.get_columns())

#transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}
dados_empresaB.rename_columns(key_mapping)
dados_fusao = Dados.join(dados_empresaA,dados_empresaB)
print(dados_fusao.dados)

#Load

dados_fusao.salvando_dados(path_dados_combinados)

