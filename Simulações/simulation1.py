import numpy as np 


def branching_bernoulli(populacao_atual, quantia_clones, geracoes, probabilidade):
    geracao_atual = populacao_atual
    lista_geraçoes = []
    lista_geracoes.append(geracao_atual)

    for i in range(geracoes):
        acumulado = 0
        for i in range(geracao_atual):
            acumulado += quantia_clones*np.random.binomial(1,probabilidade)
        lista_geracoes.append(acumulado)
        geracao_atual = acumulado
        if geracao_atual == 0:
            break

    return lista_geracoes





