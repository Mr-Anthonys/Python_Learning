# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Simule uma cafeteira orientada a objetos

#Classe generica BebidaQuente {abstract}
    #preparar()
    #fever_agua()
    #misturar() {abstract}
    #servir() {abstract}

#Sub Classes
# 1Cafe
    #misturar()
    #servir()

# 2Cha
    #misturar()
    #servir()

# 3Leite
    #misturar()
    #servir()


from rich.panel import Panel
from rich import print


conteudo = Panel(" [italic bold white] conteudos prepadaos [/] ",
                             title="[red]-Caféteria-[/]",
                             style= "cyan",
                             width= 40)


print(conteudo)
    