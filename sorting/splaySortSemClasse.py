# from numba import njit
#@njit(parallel=True)
def criar_no(chave):
    return [chave, None, None]  # nó representado por uma lista [chave, esquerda, direita]

#@njit(parallel=True)
def rotacionar_dir(x, counter_comparisons, counter_moviments):
    counter_moviments += 3
    y = x[1]
    x[1] = y[2]
    y[2] = x
    return y, counter_comparisons, counter_moviments

#@njit(parallel=True)
def rotacionar_esq(x, counter_comparisons, counter_moviments):
    counter_moviments += 3
    y = x[2]
    x[2] = y[1]
    y[1] = x
    return y, counter_comparisons, counter_moviments

#@njit(parallel=True)
def splay(raiz, chave, counter_comparisons, counter_moviments):

    counter_comparisons += 1
    if raiz is None or raiz[0] == chave:
        return raiz

    counter_comparisons += 1
    if raiz[0] > chave:

        counter_comparisons += 1
        if raiz[1] is None:
            return raiz
        
        if raiz[1][0] > chave:
            counter_comparisons += 1

            if raiz[1][1] is not None:
                counter_comparisons += 1

                counter_moviments += 1
                raiz[1][1], counter_comparisons, counter_moviments = splay(raiz[1][1], chave, counter_comparisons, counter_moviments)

            counter_moviments += 1
            raiz, counter_comparisons, counter_moviments = rotacionar_dir(raiz, counter_comparisons, counter_moviments)
            
        elif raiz[1][0] < chave:
            counter_comparisons += 1

            if raiz[1][2] is not None:
                counter_comparisons += 1

                counter_moviments += 1
                raiz[1][2], counter_comparisons, counter_moviments = splay(raiz[1][2], chave, counter_comparisons, counter_moviments)

            if raiz[1][2] is not None:
                counter_comparisons += 1

                counter_moviments += 1
                raiz[1], counter_comparisons, counter_moviments = rotacionar_esq(raiz[1], counter_comparisons, counter_moviments)

        counter_comparisons += 1
        if raiz[1] is not None:
            counter_moviments += 1
            raiz, counter_comparisons, counter_moviments = rotacionar_dir(raiz, counter_comparisons, counter_moviments)

            return raiz, counter_comparisons, counter_moviments
        else:
            return raiz, counter_comparisons, counter_moviments
        
    else:
        counter_comparisons += 1
        if raiz[2] is None:
            return raiz

        if raiz[2][0] > chave:
            counter_comparisons += 1

            if raiz[2][1] is not None:
                counter_comparisons += 1

                counter_moviments += 1
                raiz[2][1], counter_comparisons, counter_moviments = splay(raiz[2][1], chave, counter_comparisons, counter_moviments)

            if raiz[2][1] is not None:
                counter_comparisons += 1

                counter_moviments += 1
                raiz[2], counter_comparisons, counter_moviments = rotacionar_dir(raiz[2], counter_comparisons, counter_moviments)

        elif raiz[2][0] < chave:
            counter_comparisons += 1

            if raiz[2][2] is not None:
                counter_comparisons += 1

                counter_moviments += 1
                raiz[2][2], counter_comparisons, counter_moviments = splay(raiz[2][2], chave, counter_comparisons, counter_moviments)

            counter_moviments += 1
            raiz, counter_comparisons, counter_moviments = rotacionar_esq(raiz, counter_comparisons, counter_moviments)

        counter_comparisons += 1
        if raiz[2] is not None:

            counter_moviments += 1
            raiz, counter_comparisons, counter_moviments = rotacionar_esq(raiz, counter_comparisons, counter_moviments)
            return raiz, counter_comparisons, counter_moviments
        else:
            return raiz, counter_comparisons, counter_moviments

#@njit(parallel=True)
def insere(raiz, chave, counter_comparisons, counter_moviments):
    counter_comparisons += 1
    if raiz is None:
        return criar_no(chave)

    counter_moviments += 1
    raiz, counter_comparisons, counter_moviments = splay(raiz, chave, counter_comparisons, counter_moviments)

    counter_comparisons += 1
    if raiz[0] == chave:
        return raiz

    novo_no = criar_no(chave)

    counter_comparisons += 1
    if raiz[0] > chave:

        counter_moviments += 3
        novo_no[2] = raiz
        novo_no[1] = raiz[1]
        raiz[1] = None
    else:

        counter_moviments += 3
        novo_no[1] = raiz
        novo_no[2] = raiz[2]
        raiz[2] = None

    return novo_no, counter_comparisons, counter_moviments

#@njit(parallel=True)
def deleta(raiz, chave, counter_comparisons, counter_moviments):

    counter_comparisons += 1
    if raiz is None:
        return None

    counter_moviments += 2
    raiz, chave, counter_comparisons, counter_moviments = splay(raiz, chave, chave, counter_comparisons, counter_moviments)

    counter_comparisons += 1
    if raiz is None or chave != raiz[0]:
        return raiz
    
    counter_comparisons += 1
    if raiz[1] is None:
        return raiz[2]
    else:
        counter_moviments += 4
        temp = raiz
        raiz, chave, counter_comparisons, counter_moviments = splay(raiz[1], chave, chave, counter_comparisons, counter_moviments)
        raiz[2] = temp[2]

    return raiz, counter_comparisons, counter_moviments

#@njit(parallel=True)
def minimo(raiz, counter_comparisons, counter_moviments):

    counter_comparisons += 1
    if raiz is None:
        return None

    counter_moviments += 1
    no = raiz


    while no[1] is not None:
        counter_comparisons += 1

        counter_moviments += 1
        no = no[1]

    return no[0], counter_comparisons, counter_moviments

#@njit(parallel=True)
def extrai_minimo(raiz, counter_comparisons, counter_moviments):

    counter_comparisons += 1
    if raiz is None:
        return None, None

    counter_moviments += 1
    min_chave, counter_comparisons, counter_moviments = minimo(raiz, counter_comparisons, counter_moviments)

    counter_moviments += 1
    raiz, counter_comparisons, counter_moviments = deleta(raiz, min_chave, counter_comparisons, counter_moviments)

    return min_chave, raiz, counter_comparisons, counter_moviments

#@njit(parallel=True)
def splaySort(A):

    counter_comparisons = 0
    counter_moviments = 0

    raiz = None
    for x in A:
        counter_moviments += 1
        raiz, counter_comparisons, counter_moviments = insere(raiz, x, counter_comparisons, counter_moviments)

    B = []
    while raiz is not None:
        counter_comparisons += 1

        counter_moviments += 1
        min_valor, raiz, counter_comparisons, counter_moviments = extrai_minimo(raiz, counter_comparisons, counter_moviments)

        B.append(min_valor)
    return B, counter_comparisons, counter_moviments

# Exemplo de uso:
A = [5, 2, 8, 1, 3]
B = splaySort(A)
print(B)  # Esperado: [1, 2, 3, 5, 8]
