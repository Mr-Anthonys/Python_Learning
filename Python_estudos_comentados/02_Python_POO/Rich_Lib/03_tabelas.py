# ============================================================
# Estudos da biblioteca Rich
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from rich import print as rprint
from rich.table import Table

tabela = Table(title='⨚_†HELL†_⨙ ', style="bold red")
tabela.add_column(" _₼_[bold italic]NOME[/]_₼_", justify='center',)         # ⩙ ⨁ ⨷ ⨴ ⨖ † ૱ ¥ ₰ ₼
tabela.add_column("†_PECADO_†", justify='center', style="black")

tabela.add_row('Yeshua', 'G⨁D')




rprint(tabela)







# from rich.console import Console
# from rich.table import Table

# console = Console()

# # Criação da tabela
# tabela = Table(
#     title="Relatório",
#     show_lines=True,        # linhas divisórias entre cada linha
#     header_style="bold white on blue",
#     border_style="bright_black",
#     caption="Atualizado hoje",
# )

# # Adicionando colunas (ESSENCIAL para a tabela aparecer)
# tabela.add_column("ID", justify="center", style="cyan")
# tabela.add_column("Nome", style="magenta")
# tabela.add_column("Status", style="green")

# # Adicionando algumas linhas de exemplo
# tabela.add_row("01", "Projeto Alpha", "Concluído")
# tabela.add_row("02", "Projeto Beta", "Em andamento")

# # Exibindo no console
# console.print(tabela)

# # tabela = Table(title="Usuários")

# # tabela.add_column("Nome", style="cyan", no_wrap=True)
# # tabela.add_column("Idade", justify="right", style="magenta")
# # tabela.add_column("Cidade", style="green")

# # tabela.add_row("Ana", "28", "São Paulo")
# # tabela.add_row("Bruno", "35", "Rio de Janeiro")
# # tabela.add_row("Carla", "22", "Belo Horizonte")

# # console.print(tabela)

