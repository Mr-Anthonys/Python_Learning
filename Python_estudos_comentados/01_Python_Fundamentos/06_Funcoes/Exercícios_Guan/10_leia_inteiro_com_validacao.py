# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# leiaint(), uma validação para aceitar apenas valor numérico.
#CORES
#region
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
#endregion

# Lê uma entrada e procura garantir que ela seja um número inteiro válido.
def leiaint():
    while True:
        entrada = input('Nº: ')
        try:

            n = int(entrada)        
            print(f'Valor{BOLD}{GREEN}{UNDER} {n} {RESET}aceito ! ')
            break
        except (TypeError, ValueError):
            print(f'Valor{RED}{UNDER}{BOLD} {entrada}{RESET} inválido\nInforme números inteiros. !')
    return n 


n1 = leiaint()
print(f'Valor adicionado e verificado com sucesso.')
n2 = leiaint()
print(f'Valor adicionado e verificado com sucesso.')

print(f'Os valores foram n = {n1}  e n2 = {n2}\n Podemos usalos.')