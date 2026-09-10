# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from functools import singledispatchmethod

# A classe `Carteira` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Carteira:
    def __init__(self, saldo:float = None):
        self.__saldo = None
        self.saldo = saldo 


    @property
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def saldo(self): # Getter
        return f'SALDO = {self.__saldo:,.2f}'

    @saldo.setter
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def saldo(self, valor:float): # Setter
        if valor > 0 and isinstance(valor, float):
            self.__saldo = valor
            return self.__saldo


