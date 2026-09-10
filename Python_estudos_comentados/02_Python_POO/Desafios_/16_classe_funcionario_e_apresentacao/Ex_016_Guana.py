# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from rich import print, inspect

# A classe `Funcionario` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Funcionario:
    # Aributos de CLASSE --> Todos os objetos da classe vão receber esse atributo (seria algo comum em todos os objetos)

    empresa = 'Kali_Linux' # Atributo que todos os objetos vão possuir.



    # Metodo construtor / Metodo Iniciador
    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome, setor, cargo):

        # Atributos de instância (atributos que os objetos vão receber) Cada objeto com seu atributo particular.
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    # Métodos 
    def Apresentaçao(self) -> str: # Antes dos : use -> e o tipo que o método está retornando no caso (STR)
        return f'Olá sou [magenta]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa [green]{Funcionario.empresa}[/]'# Chamando o atributo da classe pra esse objeto
                                                                                                                                        # sintaxe:
                                                                                                                                        # "nome da classe" . variavel
                                                                                                                                        # "self.__class__" . variavel

                                                                                                                                        # Funcionario.empresa
                                                                                                                                        # self.__class__.empresa 


# Objetos
c1 = Funcionario('Guilherme', 'T.I', 'Eng-Softwere')
c2 = Funcionario('José', 'T.I', 'Chefe')
print(c1.Apresentaçao())
print(c2.Apresentaçao())

inspect(c1)
inspect(c2)
inspect(Funcionario) # Verificando os atributos DA CLASSE (universal para todos os objetos)

# Exibindo os atributos do objeto em forma de dicionário.
#print(c1.__dict__)

# Função inspect() da lib rich, inspeciona o objeto e exibe de uma maneira mais limpa os atributos.
#inspect(c1)
#inspect(c1, methods=True)# Add a exibição dos métodos
#inspect(c1, dunder=True)# Add a exibição dos métodos DUNDER ( __ ) 2 Underscore



