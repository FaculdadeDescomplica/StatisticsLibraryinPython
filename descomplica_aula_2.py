# -*- coding: utf-8 -*-
"""Descomplica Aula 2"""

#instalando a API
!pip install yfinance

#importando a biblioteca
import yfinance as yf
import pandas as pd
import numpy as np

#pegar a ação que queremos trabalhar
acao = yf.Ticker("PETR4.SA")
data = acao.history(period='1y')
data

"""Usamos a função filter com o parâmetro items para filtrar as colunas que queremos.
Importante: Deve-se usar dentro de colchete [ ] pois é esperado como entrada uma lista.

"""

#filter
df = data.filter(items=['Open'])
df

#filter
df = data.filter(items=['Open','Close'])
df

"""O parametro axis=1 ou 'columns' informa que queremos usar a coluna e axis=0 ou 'index' informa que queremos usar a linha. O default é ‘None’ que utiliza a coluna."""

df = data.filter(like='gh', axis = 1)
df

df = data[(data.index > '2022-09-14')]
df

#drop
df = data.drop(['High','Low'], axis = 1 )
df

#Drop linhas
df = data.drop(['2022-09-14','2022-09-15'], axis = 0)
df

"""# MAP

O comando map é usado nas colunas do pandas uma vez que cada coluna é considerada um Series. Uma Series é uma matriz de apenas uma coluna, como se fosse uma lista, que possui seus tipos definidos (podendo ser de um só tipo ou uma combinação deles), índices (podendo ser uma número como já vimos ou definido por nós como string ou uma lista) e pode ter um nome (como os nomes das colunas no nosso dataframe).
A função map é utilizada para substituir valores de uma series, e aceita como argumentos de entradas um dicionário ou uma serie ou outra função.
"""

#map toda a coluna
df['New_Dividends_map'] = data['Dividends'].map({0:2.00})
df

#map apenas na data estabelecidsa
df['New_Dividends_map'] = data['Dividends'].map({0:2.00}).where(data.index == '2022-10-05')
df

"""# REPLACE"""

bova = pd.read_csv('/content/all_bovespa.csv', delimiter=';')

bova

df_petr = bova[bova['sigla_acao'] == 'PETR4' ]
df_petr

#replace coluna nome acao
df_petr['nome_acao'] = df_petr['nome_acao'].replace('PETROBRAS', 'PETROBRAS.SA')
df_petr

df_petr['preco_maximo'] = df_petr['preco_maximo'].replace(34.66,35.00)
df_petr

df_sample = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                    'B': [5, 6, 7, 8, 9],
                    'C': ['a', 'b', 'c', 'd', 'e']})
df_sample

df_sample.replace([0, 1, 2, 3], 4)

df_sample.replace({'A': 0, 'B': 5}, 100)

"""# DADOS FALTANTES"""

#criar um dataframe
df_missing = pd.DataFrame({'A': [0, 1, 2, None, 4],
                    'B': [5, 6, None, 8, 9],
                    'C': ['a', 'b', 'a', 'a', None]})
df_missing

#verificar se tem nulos
df_missing.isnull()

#verificar se tem nulos
df_missing.isnull().sum()

#prencher com a media
media =  df_missing['A'].mean()
df_missing = df_missing['A'].fillna(media)
df_missing

media =  df_missing['A'].mean()
mediana =  df_missing['B'].median()
moda = df_missing['C'].mode()[0]
df_missing =  df_missing.fillna(value={'A':media,'B':mediana, 'C':moda})
df_missing