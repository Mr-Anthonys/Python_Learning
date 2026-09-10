# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from pessoa import Pessoa

# A classe `Funcionario` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Funcionario(Pessoa):
    """Classe Funcionário é uma Pessoa(), e possui cargo, setor
    Metodo adicional: Baterponto()"""
    
    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo 
        self.setor = setor 

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def bater_ponto(self):
        print(f'Funcionário {self.nome} bateu o ponto. ')