# ============================================================
# Estudos da biblioteca Rich
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# from rich import print as rprint

# print('Olá [bold red]Mundo[/]')

# rprint(f"[green]Olá [bold red]mundo[/]")

# rprint("[bold]negrito[/bold]")
# rprint("[italic]itálico[/italic]")
# rprint("[underline]sublinhado[/underline]")
# rprint("[reverse]invertido (fundo/texto trocados)[/reverse]")
# rprint("[strike]riscado[/strike]")
# rprint("[dim]esmaecido[/dim]")
# rprint("[blink]piscando[/blink]")


# rprint("[red]texto vermelho[/red]")
# rprint("[white on blue]texto branco fundo azul[/white on blue]")
# rprint("[bold magenta on black]combo completo[/bold magenta on black]")


from rich.console import Console
from rich.style import Style

console = Console()
estilo_alerta = Style(color="yellow", bold=True, underline=True)
console.print("Atenção!", style=estilo_alerta)

console.print("Erro crítico", style="bold white on red")
console.print("Sucesso", style="bold green")
console.print("Aviso", style="bold yellow")


console.print("Item", "valor", sep=" -> ")
console.print("Centralizado", justify="center")



# Tabelas 
from rich.table import Table

tabela = Table(title="Usuários")

tabela.add_column("Nome", style="cyan", no_wrap=True)
tabela.add_column("Idade", justify="right", style="magenta")
tabela.add_column("Cidade", style="green")

tabela.add_row("Ana", "28", "São Paulo")
tabela.add_row("Bruno", "35", "Rio de Janeiro")
tabela.add_row("Carla", "22", "Belo Horizonte")

console.print(tabela)




# tabela = Table(
#     title="Relatório",
#     show_lines=True,        # linhas divisórias entre cada linha
#     header_style="bold white on blue",
#     border_style="bright_black",
#     caption="Atualizado hoje",
# )

# Painel
from rich.panel import Panel

console.print(Panel("Conteúdo importante", title="Aviso", border_style="red"))
console.print(Panel.fit("Ajusta ao tamanho do texto"))


# Painel em Colunas
from rich.columns import Columns

itens = [f"Item {i}" for i in range(20)]
console.print(Columns(itens))


# Barra de Processo
from rich.progress import Progress
import time

from rich.progress import track

for item in track(range(20), description="Trabalhando..."):
    time.sleep(0.1)

with Progress() as progress:
    tarefa = progress.add_task("[cyan]Processando...", total=100)
    while not progress.finished:
        progress.update(tarefa, advance=5)
        time.sleep(0.1)

# Varias Barras de processo
with Progress() as progress:
    t1 = progress.add_task("[red]Download", total=100)
    t2 = progress.add_task("[green]Processamento", total=100)
    t3 = progress.add_task("[cyan]Upload", total=100)

    while not progress.finished:
        progress.update(t1, advance=1.5)
        progress.update(t2, advance=1.0)
        progress.update(t3, advance=0.8)
        time.sleep(0.05)


# Loggin 

import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    handlers=[RichHandler()]
)

log = logging.getLogger("meu_app")
log.info("Aplicação iniciada")
log.warning("Isso é um aviso")
log.error("Isso é um erro")


