# -*- coding: utf-8 -*-
"""Descomplica aula 4 """

#conceito de lista
frutas = [ 'maça', 'abacaxi', 'banana' ]
frutas

frutas[0]

frutas[0:2]

frutas[0:3]

#do inicio até a posicáo 2
frutas[:2]

#do indice 1 ao final da lista
frutas[1:]

#ultimo elemento da lista
frutas[-1]

import pandas as pd

df_acoes = pd.read_csv("/content/all_bovespa.csv", delimiter=';')

df_acoes

#filtrar ações do itau
df_itau = df_acoes[df_acoes['sigla_acao'] == "ITUB4"]
df_itau

"""# LOC
Para usar o **loc** podemos pegar todos os registros de uma determianda coluna pelo nome da coluna.
o primeiro parametro indica quais as linhas que desejamos retornar e o segundo qual coluna.
"""

#loc
df1 = df_itau.loc[:,'data_pregao']
df1

df2= df_itau.loc[455:3776,'data_pregao']
df2

df3 = df_itau.loc[455:3776,['data_pregao', 'preco_abertura', 'preco_fechamento']]
df3

"""# Iloc
O comando iloc ( integer location) faz a mesma coisa que o loc porem você só consegue utilizar os indices, tanto para as linhas quanto para as colunas.
"""

df1 = df_itau.iloc[:, 1]
df1

#acessando a primeira linha do df
df2 = df_itau.iloc[0]
df2

df2 = df_itau.iloc[0:1,:]
df2

#todas as linhas e 2 colunas
df3 = df_itau.iloc[:, 2:4]
df3

df4 = df_itau.iloc[1:3, 2:4]
df4

"""Mas o nosso dataframe do itau está com index estranhos? na verdade ele permaneceu com os indexes originais.

Vamos ajustar para colocar os indices começando novamente do zero
"""

#comando reset_index()
df_itau.reset_index()

df_itau.reset_index(drop=True)

#pegar todas as linhas da primeira coluna
df_itau.loc[1:10,'data_pregao']

"""Não funcionou? Porque ? Porque essa mudança não é feita do data frame original, pois o pandas não altera o original por default, temos que inserir um argumeto para que ocorre essa alteração no data frame"""

df_itau

df_itau.reset_index(inplace=True, drop=True)

df_itau

#pegar todas as linhas da primeira coluna
df_itau.loc[1:10,'data_pregao']

"""Se quisermos mudar o indice do data frame podemos fazer isso da seguinte maneira"""

#criando um dataframe
empresa = {'email': ['jose@email.com', 'maria@email.com', 'antonio@email.com'],
   'departamento': ['marketing','financeiro','contabilidade'],
   'nome': ['Jose','Ana','Antonio']}

df_empresa = pd.DataFrame(empresa)
df_empresa

#mudando o email para o index
df_empresa.set_index('email')

df_empresa

"""Não mudou, pois essa mudança não é feita no data frame original, pois o pandas não altera o original por default, temos que inserir um argumeto para que ocorre essa alteração no data frame

"""

df_empresa.set_index('email', inplace=True)

df_empresa

df_empresa.loc['maria@email.com']

"""Dá para reverter?"""

df_empresa.reset_index

df_empresa

df_empresa.reset_index(inplace=True)

df_empresa