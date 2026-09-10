# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from rich import print, inspect
from time import sleep
# A classe `Livro` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f':open_book: [blue]Você acabou de abrir o livro "{self.titulo}"\n',
              f'Que tem [red]{self.total_paginas} páginas no total.[/]\n',
              f'Você agora está [green] na página {self.pagina_atual} [/]')


    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def avançar(self, qnt=1):
        contador = 0
        for pg in range(0, qnt, 1):
            if not self.fim_livro():
                self.pagina_atual += 1                
                print(f'Pág {self.pagina_atual} →',end=' ')
                sleep(0.55)
                contador += 1

        print(f'\nVocê avançou [yellow]{contador} páginas[/] e agora está [green]na página {self.pagina_atual} [/]')

        if self.fim_livro:
            print(f':closed_book: [red] Você chegou ao final do livro "{self.titulo}"[/]')

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def fim_livro(self) -> bool:
        #Return True if self.pagina_atual == self.total_paginas else False
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False



l1 = Livro('DICAS PYTHON', 30)
l1.avançar(31)