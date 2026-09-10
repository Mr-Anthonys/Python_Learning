# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Classe PRODUTO, onde podemos cadastrar NOME e PREÇO.
# Crie também um método que mostre etiqueta de preço do produto.
from rich.panel import Panel
from rich import print


# A classe `Produto` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Produto():
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço


    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def etiqueta(self):
        p_etiqueta = Panel.fit(
            f"[white]{self.nome.title()}[/] --> [bold green]R$:{self.preço:,.2f}[/] ",
            title= f'<_ETIQUETA DE PREÇOS_>',
            style="yellow1"
        )
        print(p_etiqueta)


  



caneta = Produto('Caneta', 1.95)
notebook = Produto('Notebook', 4999)
caneta.etiqueta()
notebook.etiqueta()

entrada_nome = input(f'Informe o nome do produto p/ cadastro: ').strip().lower()
entrada_preco = float(input(f'Informe o preço do {entrada_nome}: ').strip().lower())


personalizado = Produto(entrada_nome, entrada_preco)
personalizado.etiqueta()
