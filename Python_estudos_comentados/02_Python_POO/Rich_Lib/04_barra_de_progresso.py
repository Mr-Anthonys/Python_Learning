# ============================================================
# Estudos da biblioteca Rich
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# # Barra de Processo
# from rich.progress import Progress
# import time

# from rich.progress import track

# # for item in track(range(20), description="Trabalhando..."):
# #     time.sleep(0.1)

# # Varias Barras de processo
# with Progress() as progress:
#     t1 = progress.add_task("[red]Download", total=100)
#     t2 = progress.add_task("[green]Processamento", total=100)
#     t3 = progress.add_task("[cyan]Upload", total=100)

#     while not progress.finished:
#         progress.update(t1, advance=1.5)
#         progress.update(t2, advance=1.0)
#         progress.update(t3, advance=0.8)
#         time.sleep(0.05)

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