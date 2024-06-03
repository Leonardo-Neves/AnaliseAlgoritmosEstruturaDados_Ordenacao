# from numba import njit
#@njit(parallel=True)
def criar_no(chave):
    return [chave, None, None]  # nó representado por uma lista [chave, esquerda, direita]

#@njit(parallel=True)
def rotacionar_dir(x):
    y = x[1]
    x[1] = y[2]
    y[2] = x
    return y

#@njit(parallel=True)
def rotacionar_esq(x):
    y = x[2]
    x[2] = y[1]
    y[1] = x
    return y

#@njit(parallel=True)
def splay(raiz, chave):
    if raiz is None or raiz[0] == chave:
        return raiz

    if raiz[0] > chave:
        if raiz[1] is None:
            return raiz

        if raiz[1][0] > chave:
            if raiz[1][1] is not None:
                raiz[1][1] = splay(raiz[1][1], chave)
            raiz = rotacionar_dir(raiz)
        elif raiz[1][0] < chave:
            if raiz[1][2] is not None:
                raiz[1][2] = splay(raiz[1][2], chave)
            if raiz[1][2] is not None:
                raiz[1] = rotacionar_esq(raiz[1])

        return rotacionar_dir(raiz) if raiz[1] is not None else raiz
    else:
        if raiz[2] is None:
            return raiz

        if raiz[2][0] > chave:
            if raiz[2][1] is not None:
                raiz[2][1] = splay(raiz[2][1], chave)
            if raiz[2][1] is not None:
                raiz[2] = rotacionar_dir(raiz[2])
        elif raiz[2][0] < chave:
            if raiz[2][2] is not None:
                raiz[2][2] = splay(raiz[2][2], chave)
            raiz = rotacionar_esq(raiz)

        return rotacionar_esq(raiz) if raiz[2] is not None else raiz

#@njit(parallel=True)
def insere(raiz, chave):
    if raiz is None:
        return criar_no(chave)

    raiz = splay(raiz, chave)

    if raiz[0] == chave:
        return raiz

    novo_no = criar_no(chave)

    if raiz[0] > chave:
        novo_no[2] = raiz
        novo_no[1] = raiz[1]
        raiz[1] = None
    else:
        novo_no[1] = raiz
        novo_no[2] = raiz[2]
        raiz[2] = None

    return novo_no

#@njit(parallel=True)
def deleta(raiz, chave):
    if raiz is None:
        return None

    raiz = splay(raiz, chave)

    if raiz is None or chave != raiz[0]:
        return raiz

    if raiz[1] is None:
        return raiz[2]
    else:
        temp = raiz
        raiz = splay(raiz[1], chave)
        raiz[2] = temp[2]

    return raiz

#@njit(parallel=True)
def minimo(raiz):
    if raiz is None:
        return None

    no = raiz
    while no[1] is not None:
        no = no[1]
    return no[0]

#@njit(parallel=True)
def extrai_minimo(raiz):
    if raiz is None:
        return None, None

    min_chave = minimo(raiz)
    raiz = deleta(raiz, min_chave)
    return min_chave, raiz

#@njit(parallel=True)
def splay_sort(A):
    raiz = None
    for x in A:
        raiz = insere(raiz, x)

    B = []
    while raiz is not None:
        min_valor, raiz = extrai_minimo(raiz)
        B.append(min_valor)
    return B

# Exemplo de uso:
A = [5, 2, 8, 1, 3]
B = splay_sort(A)
print(B)  # Esperado: [1, 2, 3, 5, 8]
