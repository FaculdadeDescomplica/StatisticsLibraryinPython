# -*- coding: utf-8 -*-
"""Descomplica Aula 8 """

import numpy as np

#criando um array

d= [1,2,3,45,5]
arr = np.array(d)
arr

#checar tipo
arr.dtype

#verificando o formato
np.shape(arr)

d2 = [[1,3,5,7], [3,55,6,90]]
arr1 = np.array(d2)
arr1

np.shape(arr1)

# Get number of elements
arr.size

#acessar um elemento pela linha de coluna [l, c]

arr1[1, 2]

#Pegar uma linha do array
arr1[0,:]

arr1[1,:]

arr1[1,1:3]

#pegar linhas na ordem desejada
arr1[[1,0]]

#pegar linhas do final para o inicio
arr1[[-1]]

"""#Inicializando um array"""

#vazio
np.empty(6, dtype='int32')

np.empty([2,2], dtype='int32')

np.zeros([2,2], dtype='int32')

np.ones([2,2], dtype='int32')

#Array aleatorios
#randint é para gerar inteiros aleatoriamente
np.random.randint(0,57, size=(3,3))

#Array aleatorios
#rand é para gerar float aleatoriamente
np.random.rand(3,3)

"""# Operações Matematicas"""

arr1

arr3 = arr1 * 2 #( - , + , /)
arr3

arr33 = arr1 + 2 #( - , + , /)
arr33

arr333 = arr1 / 2 #( - , + , /)
arr333

subarr = np.subtract(arr3,arr1)
subarr

arr1.mean() # media total
arr1.mean(axis=0) # media da linha
arr1.mean(axis=1) # media da linha

max_valor_por_elemento = np.maximum(arr1,arr3)
max_valor_por_elemento

#Soma cumulativa
arr1.cumsum(axis=1)

"""Transformações"""

arr4 = np.arange(8)
arr4

arr5 = arr4.reshape(4,2)
arr5

arr6 = arr5.reshape(2,4)
arr6

#Transposta
arr7 = arr6.T
arr7

#concatenar
arr8 = np.concatenate((arr5, arr7))
arr8

np.split(arr7, 2)

#importar
arr9 = np.genfromtxt('array.txt', delimiter=',')