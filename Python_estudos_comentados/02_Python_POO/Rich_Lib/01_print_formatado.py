# ============================================================
# Estudos da biblioteca Rich
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from rich import print as rprint
#A sintaxe [estilo]texto[/estilo]
rprint("Isso é [bold red]vermelho e negrito[/bold red]")
rprint("Isso é [italic cyan]itálico ciano[/italic cyan]")


rprint("[bold]negrito[/bold]")
rprint("[underline]sublinhado[/underline]")
rprint("[strike]riscado[/strike]")


rprint("[white on blue]texto branco fundo azul[/white on blue]")