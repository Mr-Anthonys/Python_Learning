# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Exercício 5 - Sistema Bancário
# Crie as funções: depositar(), sacar(), consultar_saldo().
# Utilize uma variável chamada saldo.
# Monte um menu:
# 1 - Depositar
# 2 - Sacar
# 3 - Consultar saldo
# 4 - Sair
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
B_GREEN = "\033[42m"
#endregion
from time import sleep
# Funções: 

# Realiza a operação `depositar` sobre os dados do objeto, aplicando as regras definidas no exercício.
def depositar(depo):
    resultado_depo = saldo + depo
    return resultado_depo

# Realiza a operação `sacar` sobre os dados do objeto, aplicando as regras definidas no exercício.
def sacar(saque):
    resultado_saque = saldo - saque
    if resultado_saque >= 0:
        return resultado_saque
    else:
        print(f'{RED}SALDO INSUFICIENTE!{RESET}')
        return saldo  # devolve o saldo inalterado
    
# Função/método responsável pela operação indicada pelo nome dentro deste exercício.
def consultar_saldo(saldo):
    return saldo

saldo = 0
while True:
    
    #MENU
    print(f'{YELLOW}{"="*20}{RESET}')
    print(f'{YELLOW}{"MENU":^20}{RESET}')
    print(f'{YELLOW}{"="*20}{RESET}')
    print(f'{BOLD}1{RESET} - Depositar')
    print(f'{BOLD}2{RESET} - Sacar')
    print(f'{BOLD}3{RESET} - Consultar Saldo')
    print(f'{BOLD}4{RESET} - Sair')
    print(f'{YELLOW}{"="*20}{RESET}')

    resp = int(input(f'{CYAN}Escolha uma opção: {RESET}'))

    if resp == 1:
        sleep(1)
        print(f'{GREEN}{"DEPOSITO":_^20}{RESET}')
        
        entrada_deposito = float(input('VALOR DO DEPOSITO R$: '))
        saldo = depositar(entrada_deposito) 
        sleep(0.5)        
        print(f'Deposito de R$:{entrada_deposito:.2f} realizado com sucesso.')
        
    elif resp == 2:
        sleep(1)
        print(f'{RED}{"SAQUE":_^20}{RESET}')
        
        entrada_saque = float(input(f'VALOR DO SAQUE R$: '))
        saldo = sacar(entrada_saque)
        print(f'Saque de R$: {entrada_saque:.2f} Realizado com sucesso.')
        
    elif resp == 3:
        sleep(1)
        print(f'{PURPLE}{"SALDO":_^20}{RESET}')
        saldo = consultar_saldo(saldo)
        print(f'SALDO R$: {saldo:.2f}')
        
    elif resp == 4:
        print(f'ATÉ LOGO ! ')
        break







