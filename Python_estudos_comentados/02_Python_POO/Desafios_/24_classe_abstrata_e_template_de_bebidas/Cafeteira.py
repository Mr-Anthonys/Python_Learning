# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from abc import ABC, abstractmethod

# A classe `BebidaQuente` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class BebidaQuente(ABC):
    def __init__(self):
        print(f'--INICIANDO O PREPARO--')      

    
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def preparar(self):
        self.fever_agua()
        self.misturar()
        self.servir_bebida()
        print(f'Bebida Finalizada.')
        print('-'*20)

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def fever_agua(self):
        print(f'Fervendo água a 100Cº')

    @abstractmethod
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def misturar(self):
        pass

    @abstractmethod
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def servir_bebida(self):
        pass



# A classe `Cafe` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def misturar(self):
        print(f'Despejar a água fervida no pó do café.')

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def servir_bebida(self):
        print(f'Servir o café em uma bela xícara.')