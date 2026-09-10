# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from rich import print, inspect
from rich.panel import Panel


# A classe `Gamer` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()


    # Adiciona uma informação à estrutura de dados usada pelo objeto ou pelo exercício.
    def add_favoritos(self, nome_game):
        self.favoritos.append(nome_game)
        

    # Organiza e exibe as informações principais do objeto.
    def ficha(self):
        conteudo_painel = f"Nome real: [black on white] {self.nome} [/]"
        conteudo_painel += f"\nJogos favoritos:"
        for n, nome_game in enumerate(self.favoritos):
            conteudo_painel += f"\n {n+1}º {nome_game}"


        box = Panel(conteudo_painel, 
                    title= f"JOGADOR <{self.nick}>",
                    style= "blue",
                    width= 40,)
        print(box)


j1 = Gamer('Guilherme Roger', 'NihIl')
j1.add_favoritos('Eden Ring')
j1.add_favoritos('Nioh 2')
j1.add_favoritos('Minecraft')

j1.ficha()

