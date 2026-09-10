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
    """
# Gafanhoto().__doc__ para acessar a documentação da classe.


Essa classe cria um Gafanhoto que é uma pessoa e possui um nome e idade.


Para criar uma nova pessoa, use
variavel = (Gafanhoto(nome, idade))
    """
    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome = '<vazio>', idade = 0):# -> Método Construtor.        
        # Atributos de Instância
        self.nome = nome 
        self.idade = idade
        # self.nome é o atributo da classe, onde todos os objetos vão ter
        # a variavem nome q esta após o self.nome = "nome" <--- Esse nome é o parametro que chegou quando o objeto foi instanciado

    # Função/método responsável pela operação indicada pelo nome dentro deste exercício.
    def aniversario(self): # self é quem chama o método (parecido com parametro da função.)
        self.idade = self.idade + 1 

    # Define a representação em texto do objeto quando ele é convertido para `str()` ou exibido com `print()`.
    def __str__(self):
        return f'O Gafanhoto {self.nome} tem {self.idade} anos.'

    # Método especial relacionado à forma como o estado do objeto é obtido.
    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'
    
# Declaração do Objeto

g1 = Gafanhoto('Guilherme', 32)
g1.aniversario()
print(g1)

print(g1.__dict__)# Atributte; Retorna um dicionário
print(g1.__getstate__())#Method; Posso personalizar o retorno

print(g1.__class__)





# print(Gafanhoto().__doc__) # Dunnder Atributte
