# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from pessoa import Pessoa
# A classe `Professor` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Professor(Pessoa):
    """
    Classe professor, derivada da ancestral (Pessoa), é uma Pessoa
    Atributos e Metodos: especialidade, nivel e dar aula()."""

    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def dar_aula(self):
        print(f'Professor {self.nome} dando aula de {self.especialidade} ! ')