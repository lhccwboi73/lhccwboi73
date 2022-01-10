# Scraping site do PCI Concursos - Retorna Lista de Concursos em um arquivo Excel.
# Para Concursos no filtro Nacional. Para Regiões é necessário mudar a url e talvez
# as tags HTML.

# Importar as bibliotecas necessárias
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Criar uma lista vazia que depois será preenchida pelo resultado da busca
lista_concursos = []

# Armazena a url dentro da variável 
pci = requests.get('https://www.pciconcursos.com.br/concursos/nacional/')

# Atribui o conteudo de pci a variável conteudo
conteudo = pci.content

# Variável que recebe o conteúdo da busca e informa ao BS o formato HTML
site = bs(conteudo, 'html.parser')

# Procura todos os dados dentro da url que contenham as tags HTML específicas
concursos = site.findAll('div', attrs={'class': 'ca'})

# Loop que extrai de cada resultado, os elementos solicitados (Titulo, Resumo e Limite)
for concurso in concursos:
    titulo = concurso.find('a', attrs={'style': 'display:block;'})
    resumo = concurso.find('div', attrs={'class': 'cd'})
    limite = concurso.find('div', attrs={'class': 'ce',})
   
    # Cria a lista de Concursos de acordo com os elementos solicitados
    lista_concursos.append([titulo.text, resumo.text, limite.text])

# Cria o Dataframe e salava o resultado dentro de um arquivo do Excel.
concursos_df = pd.DataFrame(lista_concursos, columns=['Título', 'Resumo', 'Inscrições até'])
concursos_df.to_excel('nacional.xlsx', index=False)


