# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from abc import ABC, abstractmethod
from math import pi
# A classe `Poligono` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Poligono(ABC):
    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    # Calcula a medida geométrica correspondente usando os atributos do objeto.
    def perimetro(self) -> float:
        pass
    
    @abstractmethod
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def area(self) -> float:
        pass 


# A classe `Quadrado` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Quadrado(Poligono):
    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def area(self):
        return self.lado ** 2

    # Calcula a medida geométrica correspondente usando os atributos do objeto.
    def perimetro(self):
        return self.lado * 4


# A classe `Circulo` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Circulo(Poligono):
    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def area(self):
        return pi * self.raio ** 2
    
    # Calcula a medida geométrica correspondente usando os atributos do objeto.
    def perimetro(self):
        return 2 * pi * self.raio