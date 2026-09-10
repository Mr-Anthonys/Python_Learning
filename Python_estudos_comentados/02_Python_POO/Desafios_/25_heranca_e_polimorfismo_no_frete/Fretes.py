# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from abc import ABC, abstractmethod

# A classe `Transporte` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0
        
    @abstractmethod
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def calc_frete(self):
        pass
    


# A classe `Moto` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Moto(Transporte):
    fator = 0.70
    def __init__(self, distancia):
        super().__init__(distancia)
    
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"R${self.frete:.2f}"
        
# A classe `Caminhao` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Caminhao(Transporte):
    fator = 3.20
    def __init__(self, distancia):
        super().__init__(distancia)
        
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def calc_frete(self):
        if self.distancia >= 50:
            self.frete = Caminhao.fator * self.distancia
            return f"R${self.frete:.2f}"
        else:
            return f'Kilometragem abaixo do mínimo de 50km.'

# A classe `Drone` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Drone(Transporte):
    fator = 9.50
    def __init__(self, distancia):
        super().__init__(distancia)
    
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def calc_frete(self):
        if self.distancia > 10:
            return f"Distância máxima para frete de Drone é 10Km."
        else:
            self.frete = self.distancia * Drone.fator
            return f"R${self.frete:.2f}"
    
