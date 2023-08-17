# -*- coding: utf-8 -*-
"""Descomplica aula 5 """

import pandas as pd
import numpy as np
df = pd.read_excel("/content/planilha_vendas.xlsx")
df

"""pandas.crosstab(index, columns, values=None, rownames=None, colnames=None, \
                aggfunc=None, margins=False, margins_name: str = 'All', \
                dropna: bool = True, normalize=False)

1.  index: Valores para agrupar nas linhas
2.  columns: Valores para agrupar nas colunas
3.  values: Dados a serem agregados
4.  aggfunc: Função utilizada para agregar
5.  margins: Retorna o subtotal das linhas e colunas
6.  normalize: Divide os valores pela total
"""

#Criando pd.crosstab com a quantidade de pedido por pais.
pd.crosstab(df.pais,df.produto)

#Criando pd.crosstab com a quantidade de pedido por pais com subtotal por linha e coluna
pd.crosstab(df.pais,df.produto, margins=True)

#Adicionar níveis
pd.crosstab(df.pais, [df.produto,df['Garantia extendida']], margins=True)

#pedidos com garantia extendida
pd.crosstab([df.produto,df['Garantia extendida']], [df.pais] , margins=True)

#Vendas
#usar o parametro values
pd.crosstab([df.produto], [df.pais] , values=df.quantidade, margins=True)

#Quantidade  pedidos
#usar o parametro values
pd.crosstab([df.produto], [df.pais] , values=df.quantidade, aggfunc= np.sum, margins=True)

df

df['valortotal'] = df.valorunitario * df.quantidade
df2 = df.copy()
df

#Vendas
#usar o parametro values
pd.crosstab([df2.produto], [df2.pais] , values=df2.valortotal, aggfunc= np.sum, margins=True)

#% sobre o total com a função normalize:
pd.crosstab(df.pais, df.produto, normalize='index')

#% sobre o total com a função normalize ajustando o percentual:
pd.crosstab(df.pais, df.produto, normalize='index').round(4)*100

"""# Group by

"""

#agrupar por produto
df_tipo_tenis = df.groupby('produto')

df_tipo_tenis

#atributo ngroups para descobrir quantos grupos
df_tipo_tenis.ngroups

df.groupby('pais').ngroups

#atributo groups para mostrar os grupos
df.groupby('pais').groups

#atributo size para mostrar o tamanho do grupos
df.groupby('pais').size()

#atributo get_group para filtrar um grupo especifico o tamanho do grupos
df.groupby('pais').get_group('Alemanha')

df.groupby('pais').mean()

df.groupby(['pais', 'produto', ])['valortotal'].sum()

"""# Concatenar colunas

"""

clientes= pd.read_excel("/content/clientes.xlsx")
clientes

cli_prod= pd.read_excel("/content/clientes _prod.xlsx")

cli_prod

#concatenar colunas
clientes['nome_completo'] = clientes.nome + clientes.sobrenome
clientes

clientes['nome_completo'] = clientes.nome + ' ' + clientes.sobrenome
clientes

clientes['nome_completo2'] = clientes[['nome', 'sobrenome']].apply(' '.join, axis=1)
clientes

#merge
df_merge = pd.merge(clientes, cli_prod, how = 'right', on = 'id')

df_merge

"""#Concatenar dataframe"""

time1 = pd.read_excel("/content/time1.xlsx")
time1

time2 = pd.read_excel("/content/time2.xlsx")
time2

"""  #concat

Embora você possa concatenar dataframes verticalmente (eixo=0) e horizontalmente (eixo=1) usando a função Pandas.concat, sua principal vantagem está em permitir que você concatene verticalmente mais de dois DataFrame e/ou Series de uma só vez. Ao contrário de DataFrame.append, Pandas.concat não é um método, mas uma função que recebe uma lista de objetos como entrada.

Por outro lado, colunas com nomes diferentes são preenchidas com NA
"""

times_df  = pd.concat([time1,time2])
times_df

time_def_vertical = pd.concat([time1,time2], axis=0)

time_def_vertical

#inserir colunas
time_def_horizontal = pd.concat([time1,time2], axis=1)

time_def_horizontal

"""#append
Este método permite adicionar outro dataframe a um existente. Enquanto as colunas com nomes correspondentes são concatenadas, as colunas com nomes diferentes são preenchidas com NA.

É possivel resetar o indice (ignore_index= True) e ordernar os resultados
"""

times_df_append = time1.append(time2)
times_df_append



