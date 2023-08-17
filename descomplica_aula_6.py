# -*- coding: utf-8 -*-
"""Descomplica Aula 6
"""

import pandas as pd

#lendo o arquivo de ações
#Lendo csv

df = pd.read_csv("/content/all_bovespa.csv", delimiter=';')
df

#Itau filtrar
df_itau = df[df['sigla_acao'] == 'ITUB4' ]
df_itau

#verificar o tipo do arquivo
df_itau.dtypes

#Mudar o tipo data
df_itau['data_pregao'] = pd.to_datetime(df_itau['data_pregao'], format='%Y-%m-%d')

#verificar o tipo do arquivo
df_itau.dtypes

#criando novos campos de medias móveis
df_itau['mm5d'] = df_itau['preco_fechamento'].rolling(5).mean()
df_itau['mm21d'] = df_itau['preco_fechamento'].rolling(21).mean()

df_itau.head(30)

features = df_itau.drop(['sigla_acao', 'nome_acao', 'data_pregao', 'preco_fechamento','preco_abertura','mm21d'], 1)

features


from sklearn.preprocessing import MinMaxScaler
# Normalizando os dados de entrada(features)

# Gerando o novo padrão
scaler = MinMaxScaler().fit(features)
features_scale = scaler.transform(features)

print ('Features: ',features_scale.shape)
print (features_scale)# Normalizando os dados de entrada(features)


data = pd.DataFrame({'x':[1, 1.5,1.8,1.3, 35, 4.28, 2, 2.35, 3.89],
                     'y':[1, 1,2,1, 1, 1, 1, 3, 25]})
data

#grafico
import matplotlib.pyplot as plt
plt.scatter(x=data.x, y=data.y )
plt.show

import numpy as np

data['x_log'] = np.log(data['x'])
data['y_log']  = np.log(data['y'])
plt.scatter(x=data.x_log, y=data.y_log )
plt.show

"""#Outliers"""

df = pd.read_csv("//content/weight-height.csv", delimiter=',')
df

from matplotlib import pyplot as plt

plt.hist(df.Weight, bins=30, rwidth=0.8)

#maximo valores acima de 3 devios padroes

df['zscore'] = ( df.Weight - df.Weight.mean() ) / df.Weight.std()
df

df = df[(df.zscore< -3) & (df.Weight>3)]
df

"""Quando trabalhamos com dados categoricos, em nosso dataset, estamos falando de dados como sexo, caixa postal, cor. Não podemos usar esses dados diretamente em nosso modelos, eles precisam ser convertidos em numeros que representem a categoria e esse processo é chamado de enconding. Podemos fazer isso no pandas de uma maneira muito facil. Vamos vcer"""

#ler dados
df=pd.read_csv("http://bit.ly/kaggletrain")
df

#get_dummies

pd.get_dummies(df.Sex)

#criar embarque dummy
emb = pd.get_dummies(df.Embarked)
emb

#concatenar no df
df = pd.concat([df,emb],axis=1 )
df

df = pd.get_dummies(df, columns=['Sex'], drop_first=True)
df