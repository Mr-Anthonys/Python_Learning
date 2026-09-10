# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida.
# Podendo escrever frases na cor relativa.
from rich import print
# A classe `Caneta` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Caneta:
    cores = {
        'vermelho':'[red]',
        'azul':'[blue]',
        'amarelo':'[yellow]'
    }


    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, cor):

        self.cor = cor
        self.fechada = True


    # Executa uma ação específica do objeto conforme a proposta do exercício.
    def abrir(self):
        if self.fechada:
            self.fechada = False # Abriu

    # Executa uma ação específica do objeto conforme a proposta do exercício.
    def escrever(self, txt):
        if self.fechada:
            print(f'Caneta [red]FECHADA. impossivel escrever.')
        else:
            print(f'{Caneta.cores[self.cor]} {txt}[/]')


caneta1 = Caneta('azul')
caneta2 = Caneta('vermelho')

caneta1.abrir()
caneta1.escrever('Olá Mundo 2')

caneta2 = Caneta('Gatos são incriveis')


    