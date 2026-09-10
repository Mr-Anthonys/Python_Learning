# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from pessoa import Pessoa # pessoa(minusculo) é o nome do arquivo, 
                          # Pessoa (tittle) é o nome da Classe q estamos importando

# A classe `Aluno` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Aluno(Pessoa):
    """
    Classe Aluno, derivada da ancestral (é uma Pessoa) então vai herdar nome e idade e fazer aniversario
    Atributos e Metodos proprios: curso e turma, e fazer matricula()"""


    # Método Construtor do aluno

    def __init__(self, nome, idade, curso, turma):# Todos os atrib (classe pai e classe filho)
        super().__init__(nome, idade) # super() chamando o init do pai (nome, idade)

        # Atributos excusivos do Aluno
        self.curso = curso 
        self.turma = turma

        # Método exclusivo da classe derivada.
    def fazer_matricula(self):
        print(f'{self.nome} matriculado com sucesso.')