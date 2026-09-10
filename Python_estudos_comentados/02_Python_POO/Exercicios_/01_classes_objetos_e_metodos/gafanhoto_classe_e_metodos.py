# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Declaração de Classe
# A classe `Gafanhoto` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Gafanhoto:
    def __init__(self):# -> Método Construtor.        
        # Atributos de Instância
        self.nome = ''
        self.idade = 0
        self.sexo = ''
        self.peso = '0'

    # Função/método responsável pela operação indicada pelo nome dentro deste exercício.
    def aniversario(self): # self é quem chama o método (parecido com parametro da função.)
        self.idade = self.idade + 1 

    # Função/método responsável pela operação indicada pelo nome dentro deste exercício.
    def mensagem(self):
        return f'O Gafanhoto {self.nome} tem {self.idade} anos, sexo {self.sexo} e possui {self.peso}Kg.'
    
# Declaração do Objeto

g1 = Gafanhoto()
g1.nome = 'Guilherme'
g1.idade = 32
g1.sexo = 'M'
g1.peso = 70
print(g1.mensagem())


g2 = Gafanhoto()
g2.nome = 'Thais'
g2.idade = 27
g2.sexo = 'F'
g2.peso = 66
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = 'Gregory'
g3.idade = 4
g3.sexo = 'M'
g3.peso = 11
g3.aniversario()
print(g3.mensagem())
