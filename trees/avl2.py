#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
    Árvore AVL em Python
    
    Copyright (c) 2009 Vindemiatrix Almuredin.
    É dada permissão para copiar, distribuir e/ou modificar este documento
    sob os termos da Licença de Documentação FAIL,
    Versão 97.545.668.112.666.002 Build 69 Release 42;
    Uma cópia da licença talvez esteja inclusa na seção entitulada
    "Licença de Documentação FAIL".
"""

class No:
    def __init__(self, data):
        self.data = data
        self.atribui_filhos(None, None)

    def atribui_filhos(self, esquerda, direita):
        self.esquerda = esquerda
        self.direita = direita

    def balanco(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return prof_esq - prof_dir

    def profundidade(self):
        prof_esq = 0
        if self.esquerda:
            prof_esq = self.esquerda.profundidade()
        prof_dir = 0
        if self.direita:
            prof_dir = self.direita.profundidade()
        return 1 + max(prof_esq, prof_dir)

    def rotacao_esquerda(self):
        self.data, self.direita.data = self.direita.data, self.data
        old_esquerda = self.esquerda
        self.atribui_filhos(self.direita, self.direita.direita)
        self.esquerda.atribui_filhos(old_esquerda, self.esquerda.esquerda)

    def rotacao_direita(self):
        self.data, self.esquerda.data = self.esquerda.data, self.data
        old_direita = self.direita
        self.atribui_filhos(self.esquerda.esquerda, self.esquerda)
        self.direita.atribui_filhos(self.direita.direita, old_direita)

    def rotacao_esquerda_direita(self):
        self.esquerda.rotacao_esquerda()
        self.rotacao_direita()

    def rotacao_direita_esquerda(self):
        self.direita.rotacao_direita()
        self.rotacao_esquerda()

    def executa_balanco(self):
        bal = self.balanco()
        if bal > 1:
            if self.esquerda.balanco() > 0:
                self.rotacao_direita()
            else:
                self.rotacao_esquerda_direita()
        elif bal < -1:
            if self.direita.balanco() < 0:
                self.rotacao_esquerda()
            else:
                self.rotacao_direita_esquerda()

    def insere(self, data):
        if data <= self.data:
            if not self.esquerda:
                self.esquerda = No(data)
            else:
                self.esquerda.insere(data)
        else:
            if not self.direita:
                self.direita = No(data)
            else:
                self.direita.insere(data)
        self.executa_balanco()

    def imprime_arvore(self, indent = 0):
        print("(", end="")
        print(str(self.data), end="")
        #print(" " * indent + str(self.data))
        if self.esquerda:
            self.esquerda.imprime_arvore(indent + 2)
        if self.direita:
            self.direita.imprime_arvore(indent + 2)
        print(")", end="")

    def percurso_in_ordem(self):
        if self.esquerda:
            self.esquerda.percurso_in_ordem()
        print(self.data, end=" ")
        if self.direita:
            self.direita.percurso_in_ordem()

if __name__ == "__main__":
    arvore = No(10)
    arvore.insere(5)
    arvore.insere(15)
    arvore.insere(2)
    arvore.insere(7)
    arvore.insere(12)
    arvore.insere(17)
    arvore.imprime_arvore()
    print("")
    print(f"arvore.percurso_in_ordem: {arvore.percurso_in_ordem()}")
    print(f"arvore.profundidade: {arvore.profundidade()}")
    print(f"arvore.balanco: {arvore.balanco()}")
    print(f"arvore.esquerda.balanco: {arvore.esquerda.balanco()}")
    print(f"arvore.direita.balanco: {arvore.direita.balanco()}")
    print(f"arvore.esquerda.profundidade: {arvore.esquerda.profundidade()}")
    print(f"arvore.direita.profundidade: {arvore.direita.profundidade()}")

