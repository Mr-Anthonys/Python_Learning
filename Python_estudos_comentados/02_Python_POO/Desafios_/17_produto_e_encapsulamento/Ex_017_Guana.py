# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from rich import print, inspect
from rich.panel import Panel

# A classe `Produto` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Produto:
    # Método Construtor
    def __init__(self, nome, preço):

        # Atributos de instância ()
        self.nome = nome
        self.preço = preço

        # Atributo p mostrar o estado do objeto
    # Define a representação em texto do objeto quando ele é convertido para `str()` ou exibido com `print()`.
    def __str__(self):
        return f'{self.nome} custa R$:{self.preço:,.2f}'

    
    # Métodos 
    def etiqueta(self):
        conteudo_painel = f"{self.nome.center(30, ' ')}"
        conteudo_painel += f"="*30 # conteudo anterior do painel + uma linha de (30 =)
        preço_formatado = f"R${self.preço:,.2f}"
        conteudo_painel += f"{preço_formatado.center(30, '.')}"
        etiqueta = Panel(conteudo_painel, title="PRODUTO",width=34)
        print(etiqueta)
     

p1 = Produto('Head Set', 350)
p1.etiqueta()

