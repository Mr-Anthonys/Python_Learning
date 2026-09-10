# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Crie a classe Gamer, onde podemos cadastrar: NICK, NOME, JOGOS FAVORITOS.
# Crie um método que permita mostrar a ficha desse gamer.
from rich import print, inspect
from rich.panel import Panel



# A classe `Gamer` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Gamer:
    def __init__(self, nome, nick, favoritos):
        self.nome = nome
        self.nick = nick
        self.favoritos = favoritos

    
        


    # Organiza e exibe as informações principais do objeto.
    def ficha_gamer(self):
        box = Panel.fit(
            f'Jogador -> {self.nome}\n'
            f'nick = {self.nick}\n'
            f'Jogos favoritos -> {self.favoritos}',
            title=f"FICHA GAMER",
            style= "yellow"
        )
        return box

g1 = Gamer('Gui', 'NiHell', favoritos='Eldem Ring, LoL, Nioh 2, COD. ', )

print(g1.ficha_gamer())

