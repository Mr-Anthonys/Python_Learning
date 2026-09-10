# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# A classe `Pessoa` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Pessoa:
    """
    Classe ancestral, tem nome e idade da pessoa e um metodo de fazer aniversario.
    """
    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome= '', idade= 0):
        self.nome = nome
        self.idade = idade

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def fazer_aniversario(self):
        self.idade += 1