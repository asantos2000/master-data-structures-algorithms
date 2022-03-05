'''
Lista 04 - Exercício 1
Operações em lista ligada simples
'''


from http.client import NOT_MODIFIED


class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.proximo = None


class ListaLigadaSimples:
    def __init__(self):
        self.primeiro_no = None

    def imprimir(self, no=None):
        if no is None:
            no = self.primeiro_no

        print(no.dado)

        if no.proximo is None:
            return
        else:
            self.imprimir(no.proximo)

    # Adiciona nó apos o nó pivo
    # |e1|e2|e3|
    #      ^ pivo
    # |e1|e2|e4|e3|
    def inserir(self, no_pivo, novo_no):
        novo_no.proximo = no_pivo.proximo
        no_pivo.proximo = novo_no

    # Adiciona nó apos o nó na k posicao
    # |e1|e2|e3|
    #      ^ busca_no k
    # |e1|e2|e4|e3|
    def inserir_pos(self, k, novo_no):
        no_pivo = self.buscar_pos(k)
        self.inserir(no_pivo, novo_no)

    def inverter(self, no=None):
        if no is None:
            no = self.primeiro_no
        if no.proximo is None:
            self.primeiro_no = no
            return
        self.inverter(no.proximo)
        no.proximo.proximo = no
        no.proximo = None

    # def buscar_pos(self, k):
    #     no = self.primeiro_no
    #     for i in range(k):
    #         no = no.proximo
    #     return no

    def buscar_pos(self, k, no=None):
        if no is None:
            no = self.primeiro_no
        if k == 0:
            return no
        else:
            no = no.proximo
            return self.buscar_pos(k - 1, no)

    def no_meio(self):
        lento = self.primeiro_no
        rapido = self.primeiro_no

        while rapido.proximo:
            lento = lento.proximo
            rapido = rapido.proximo.proximo

        return lento.dado

    def minimo(self):
        no = self.primeiro_no
        menor = no.dado
        while no:
            if no.dado < menor:
                menor = no.dado
            no = no.proximo
        return menor

if __name__ == "__main__":
    e1 = No("A")
    e2 = No("B")
    e3 = No("C")
    lista = ListaLigadaSimples()
    lista.primeiro_no = e1
    e1.proximo = e2
    e2.proximo = e3

    print('lista')
    lista.imprimir()

    print('Insere D e E')
    e4 = No("D")
    lista.inserir(e2, e4)

    e5 = No("E")
    lista.inserir_pos(2, e5)
 
    print('nova lista')
    lista.imprimir()

    print('Busca posicao')
    print(f'Pos 0: {lista.buscar_pos(0).dado}')
    print(f'Pos 1: {lista.buscar_pos(1).dado}')
    print(f'Pos 2: {lista.buscar_pos(2).dado}')
    print(f'Pos 3: {lista.buscar_pos(3).dado}')
    print(f'Pos 4: {lista.buscar_pos(4).dado}')

    print(f'No proximo do meio: {lista.no_meio()}')

    print('lista invertida')
    lista.inverter()
    lista.imprimir()

    print(f'Imprimir a partir de {e4.dado}')
    lista.imprimir(e4)

    print('lista 1 elemento')
    e1 = No("ONE")
    lista2 = ListaLigadaSimples()
    lista2.primeiro_no = e1
    lista2.imprimir()
    lista2.inverter()
    lista2.imprimir()
    print(f'No proximo do meio: {lista2.no_meio()}')

    print('menor valor lista')
    print(f'Menor valor: {lista.minimo()}')
    print(f'Menor valor: {lista2.minimo()}')
    lista3 = ListaLigadaSimples()
    e1 = No(5)
    e2 = No(4)
    e3 = No(2)
    e4 = No(3)
    e5 = No(1)
    e1.proximo = e2
    e2.proximo = e3
    e3.proximo = e4
    e4.proximo = e5
    lista3.primeiro_no = e1
    lista3.imprimir()
    print(f'Menor valor: {lista3.minimo()}')