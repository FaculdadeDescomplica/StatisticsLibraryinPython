# -*- coding: utf-8 -*-
"""Descomplica aula 3 """

#importar as bibliotecas
import pandas as pd


#ler arquivo
df_prouni = pd.read_excel('/content/cursos-prouni.csv.xlsx')
df_prouni

pd.set_option('display.max_rows', 1000)

#value count
df_prouni['curso_busca'].value_counts()

#max
df_prouni['mensalidade'].max()

#valor medio por estado
df_prouni.groupby(['uf_busca'])['mensalidade'].agg(['sum'])

#valor medio por estado
df_prouni.groupby(['uf_busca'])['mensalidade'].agg(['mean'])

#valor medio por estado
df_prouni.groupby(['uf_busca', 'curso_busca'])['mensalidade'].agg(['mean'])

#valor medio por estado
df_prouni.groupby(['uf_busca', 'curso_busca'])['mensalidade'].agg(['mean']).sort_values(by=['uf_busca', 'mean'], ascending=False)

#criar função
def duplica_bolsa(rows):
  nova_bolsa = rows * 2
  return nova_bolsa

#usando o apply
df = df_prouni[['uf_busca', 'curso_busca','mensalidade','bolsa_integral_ampla' ]]
df

df['nova_bolsa'] = df['bolsa_integral_ampla'].apply(duplica_bolsa)

df

df['nova_bolsa'] = df['nova_bolsa'].fillna(1)
df

#lambda
df['nova_bolsa_lambda'] = df['bolsa_integral_ampla'].apply(lambda x: x * 2 )
df

#criar um novo campo com o método assign e lambda

df = df.assign(nova_bolsa_lambda2 = lambda x: (x['bolsa_integral_ampla'] * 2))

df