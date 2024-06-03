
class No:
    def __init__(self, chave):
        self.chave = chave
        self.esq = None
        self.dir = None

class SplayTree:
    def __init__(self):
        self.raiz = None

    def rotacionar_dir(self, x):
        y = x.esq
        x.esq = y.dir
        y.dir = x
        return y

    def rotacionar_esq(self, x):
        y = x.dir
        x.dir = y.esq
        y.esq = x
        return y

    def splay(self, raiz, chave):
        if raiz is None or raiz.chave == chave:
            return raiz

        if raiz.chave > chave:
            if raiz.esq is None:
                return raiz

            if raiz.esq.chave > chave:
                raiz.esq.esq = self.splay(raiz.esq.esq, chave)
                raiz = self.rotacionar_dir(raiz)
            elif raiz.esq.chave < chave:
                raiz.esq.dir = self.splay(raiz.esq.dir, chave)
                if raiz.esq.dir is not None:
                    raiz.esq = self.rotacionar_esq(raiz.esq)

            return self.rotacionar_dir(raiz) if raiz.esq is not None else raiz
        else:
            if raiz.dir is None:
                return raiz

            if raiz.dir.chave > chave:
                raiz.dir.esq = self.splay(raiz.dir.esq, chave)
                if raiz.dir.esq is not None:
                    raiz.dir = self.rotacionar_dir(raiz.dir)
            elif raiz.dir.chave < chave:
                raiz.dir.dir = self.splay(raiz.dir.dir, chave)
                raiz = self.rotacionar_esq(raiz)

            return self.rotacionar_esq(raiz) if raiz.dir is not None else raiz

    def insere(self, chave):
        if self.raiz is None:
            self.raiz = No(chave)
            return

        self.raiz = self.splay(self.raiz, chave)

        if self.raiz.chave == chave:
            return

        novoNo = No(chave)
        if self.raiz.chave > chave:
            novoNo.dir = self.raiz
            novoNo.esq = self.raiz.esq
            self.raiz.esq = None
        else:
            novoNo.esq = self.raiz
            novoNo.dir = self.raiz.dir
            self.raiz.dir = None
        self.raiz = novoNo

    def deleta(self, chave):
        if self.raiz is None:
            return

        self.raiz = self.splay(self.raiz, chave)

        if chave != self.raiz.chave:
            return

        if self.raiz.esq is None:
            self.raiz = self.raiz.dir
        else:
            temp = self.raiz
            self.raiz = self.splay(self.raiz.esq, chave)
            self.raiz.dir = temp.dir

    def minimo(self):
        if self.raiz is None:
            return None

        No = self.raiz
        while No.esq is not None:
            No = No.esq
        return No.chave

    def extrai_minimo(self):
        if self.raiz is None:
            return None

        min_chave = self.minimo()
        self.deleta(min_chave)
        return min_chave
    
    
def splaySort(A):
    tree = SplayTree()
    for x in A:
        tree.insere(x)
    
    B = []
    while tree.raiz is not None:
        B.append(tree.extrai_minimo())
    return B


A = [5, 2, 8, 1, 3]
B = splaySort(A)
print(B)
