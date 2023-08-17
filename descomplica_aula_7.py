# -*- coding: utf-8 -*-
"""Descomplica Aula 7 """

import re

"""re.match()
Esse método vai buscar a ocorrência no início de uma string.
"""

busca = re.match(r'Antonio', 'Rua Antonio Basilio')
busca

"""re.search()
Esse método vai buscar casar a ocorrência da  string independente da posição.
"""

busca = re.search(r'Antonio', 'Rua Antonio Basilio')
busca

"""re.findall()
Esse método vai retornar uma lista de todas as  ocorrência encontradas string independente da posição.
"""

busca = re.findall(r'div', '<div class=container > <div class=row >')
busca

"""re.split"""

result=re.split(r'y','Analytics')
print result

p = re.compile(r'[0-9]+')
p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')

"""Re no pandas

"""

import pandas as pd

df = pd.read_csv('/content/all_bovespa.csv', sep=';' )
df

#extrair os 5 primeiros caracteres do nome da acao
df['nome_abre']=df['nome_acao'].str.extract(r'(^w{1})')

df

reg = df.filter(regex='^preco')

reg

reg = df.filter(regex='os$')

reg



reg = df.filter(regex='preco[_].')

reg

reg = df.filter(regex='.[_].')

reg