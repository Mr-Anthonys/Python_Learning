# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from abc import ABC, abstractmethod
from rich import print, inspect

# A classe `Paligono` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Paligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    # Calcula a medida geométrica correspondente usando os atributos do objeto.
    def perimetro(self):
        pass

    @abstractmethod
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def area(self):
        pass

# A classe `Quadrado_my` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Quadrado_my(Paligono):
    def __init__(self, tam_lado, qtd_lados):
        super().__init__(qtd_lados)
        self.tam_lado = tam_lado

    # Calcula a medida geométrica correspondente usando os atributos do objeto.
    def perimetro(self):
        perimetro = self.tam_lado * self.qtd_lados
        print(f'PERIMETRO = LADO x QUANTIDADE DE LADOS')
        return perimetro

    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def area(self):
        area = self.tam_lado * 2
        print(f'AREA = LADO x LADO')
        return area

# A classe `Circulo_my` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Circulo_my(Paligono):
    def __init__(self, raio, qtd_lados):
        super().__init__(qtd_lados)
        self.raio = raio

    # Calcula a medida geométrica correspondente usando os atributos do objeto.
    def perimetro(self):
        perimetro = (self.raio * 2) * 3.14
        print(f'Calculando perimetro em circulo.\nPERIMETRO = (2 x raio) x π (3.14)')
        return perimetro

    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def area(self):
        area = (self.raio ** 2) * 3.14
        print(f'AREA = raio² x π (3.14)')
        return area

    
q1 = Quadrado_my(tam_lado= 6, qtd_lados=4)
perimetro_quadrado = q1.perimetro()
area_quadrado = q1.area()

c1 = Circulo_my(raio=3, qtd_lados=0)
perimetro_circulo = c1.perimetro()
area_circulo = c1.area()


print(f"Um circulo com raio de {c1.raio} ")
print(f'perimetro do quadrado = {perimetro_quadrado}')
print(f'Area do quadrado = {area_quadrado}')
print(f'perimetro do circulo = {perimetro_circulo}')
print(f'Area do circulo = {area_circulo}')




