# ============================================================
# Exercício/rascunho de Python
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#+-------------------+---------------------+---------------------+
#|  🎭 STYLE (Estilo)|  🔤 TEXT (Texto)    |  🧱 BACK (Fundo)    |
#+-------------------+---------------------+---------------------+
#|  0 = Normal       |  30 = Preto         |  40 = Preto         |
#|  1 = Negrito      |  31 = Vermelho      |  41 = Vermelho      |
#|  4 = Sublinhado   |  32 = Verde         |  42 = Verde         |
#|  7 = Inverter     |  33 = Amarelo       |  43 = Amarelo       |
#|                   |  34 = Azul          |  44 = Azul          |
#|                   |  35 = Roxo/Magenta  |  45 = Roxo/Magenta  |
#|                   |  36 = Ciano         |  46 = Ciano         |
#|                   |  37 = Branco        |  47 = Branco        |
#+-------------------+---------------------+---------------------+



#🐍 Snippet Pronto para Python

#CORES

# Constantes para deixar o código limpo
RESET  = "\033[0m"
BOLD   = "\033[1m"
UNDER  = "\033[4m"

# Cores de Texto
BLACK  = "\033[30m"
BLUE   = "\033[34m"
PURPLE = "\033[35m"
RED    = "\033[31m"
GREEN  = "\033[32m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"

#Cores de Fundo
B_RED   = "\033[41m"
B_BLACK = "\033[40m"
B_BLUE  = "\033[44m"
B_WHITE = "\033[47m"
B_GREEN = "\033[42m"

# Exemplos: 
print(f"{BOLD}{GREEN}[OK]{RESET} Operação concluída com sucesso!")
print(f"{BOLD}{RED}[ERRO]{RESET} Falha ao conectar ao banco.")
print(f"{UNDER}{YELLOW}[AVISO]{RESET} Verifique as configurações.")
