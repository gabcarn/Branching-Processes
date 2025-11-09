import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

def branching_bernoulli(populacao_atual, quantia_clones, geracoes, probabilidade):
    geracao_atual = populacao_atual
    lista_geraçoes = []
    lista_geraçoes.append(geracao_atual)

    for i in range(geracoes):
        acumulado = 0
        for i in range(geracao_atual):
            acumulado += quantia_clones*np.random.binomial(1,probabilidade)
        lista_geraçoes.append(acumulado)
        geracao_atual = acumulado
        if geracao_atual == 0:
            break

    return lista_geraçoes

tamanhos = []

for i in range(500):
    tamanhos.append(len(branching_bernoulli(2,4,50,0.4)))

plt.hist(tamanhos)
plt.savefig('grafico.png')

