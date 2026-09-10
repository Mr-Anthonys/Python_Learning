# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Classe funcionário, onde podemos cadastrar, NOME,SETOR e CARGO.
#Crie tabém um método que permita o funcionário se apresentar.

from rich import print
from rich.panel import Panel

# A classe `Funcionario` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    # Organiza e exibe as informações principais do objeto.
    def apresentacao(self):
        # Criando o conteúdo de texto formatado para um único painel
        conteudo = (
            f"[white]Olá, eu sou[/] [italic bold green]{self.nome}[/]\n"
            f"[white]Do setor[/] [italic bold red]{self.setor}[/]\n"
            f"[white]No cargo de[/] [bold magenta on black]{self.cargo}[/]"
        )
        
        # Exibindo tudo dentro de um painel unificado e elegante
        painel = Panel(
            conteudo, 
            title="[bold yellow]~ APRESENTAÇÃO DO FUNCIONÁRIO ~[/]", 
            style="orange1", 
            width=45,
            expand=False
        )
        print(painel)

# Coleta de dados fora da classe
nome_input = input('Nome: ')
setor_input = input('Setor: ')
cargo_input = input('Cargo: ')

# Instanciação e chamada do método
f_1 = Funcionario(nome_input, setor_input, cargo_input)
print() # Apenas para dar um espaço visual no terminal
f_1.apresentacao()

