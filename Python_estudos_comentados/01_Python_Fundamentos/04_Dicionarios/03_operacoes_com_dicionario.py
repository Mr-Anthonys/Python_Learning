# ============================================================
# Exercício de dicionários
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
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


#Exercício 92 print com replace no dicionário
#region

#Crie um programa que leia NOME,ANO de NASCIMENTO e CARTEIRA JOB.
#Cadastre-os (com idade) em um dict() 
#Se por acaso a CRPS for diferente de 0 
#O dict() receberá também o ANO DE CONTRATAÇÃO e SALÁRIO.
#Calcule com que idade vai se aposentar e com quantos anos.

from time import sleep
#-  Dicionário vazio
cadastro_dict = dict()
print(f'{UNDER}{BOLD}{PURPLE}{" ":39} ')
print(f'{BOLD}{UNDER}{PURPLE}{B_BLACK}{"_CADASTRO_":^40}{RESET}')


cadastro_dict["nome"] = str(input(f'NOME: ').strip().lower())#- Entrada do NOME
cadastro_dict["ano_nascimento"] = int(input('ANO DE NASCIMENTO: ').strip())#- Entrada da data de nasc.
cadastro_dict["idade"] = (2026 - cadastro_dict["ano_nascimento"])#- Entrada da idade (ano atual = data de nasc.)
cadastro_dict["carteira_ctps"] = int(input(f'CTPS: ').strip())#- Entrada do nº da carteira de trabalho

if cadastro_dict["carteira_ctps"] > 0:
    cadastro_dict["ano_contrataçao"] = int(input(f'ANO DE CONTRATAÇÃO: '))
    cadastro_dict["salario"] = float(input(f'SALÁRIO R$: '))


    print(f'{UNDER}{BOLD}{PURPLE}{" ":39} ')
    print(f'{BOLD}{UNDER}{PURPLE}{B_BLACK}{"APOSENTADORIA":^40}{RESET}')
    #Considerando 60 idade e 35 trabalhado

    anos_trabalhados = (2026 - cadastro_dict["ano_contrataçao"])
    print(f'==ANALISANDO==')
    sleep(1)


    if cadastro_dict["idade"] < 60 and anos_trabalhados < 35:
        sleep(1)
        print(f'{UNDER}{BOLD}{PURPLE}{" ":39} {RESET}')
        print(f'Com {anos_trabalhados} anos trabalhados.')
        print(f'{UNDER}{BOLD}{PURPLE}{" ":39} {RESET}')
        sleep(1)
        print(f'{UNDER}{BOLD}{PURPLE}{" ":39}{RESET} ')
        print(f'E {cadastro_dict["idade"]} de idade.\nAinda faltam {(60 - cadastro_dict["idade"])} anos para se aposentar.')
        print(f'{UNDER}{BOLD}{PURPLE}{" ":39}{RESET} ')
    else:
        sleep(1)
        print(f'{UNDER}{BOLD}{PURPLE}{" ":39}{RESET} ')
        print(f'PARÁBENS !!\nCom {cadastro_dict["idade"]}anos.\nE {anos_trabalhados} anos trabalhados.\nVocê ja pode se aposentar')
        print(f'{UNDER}{BOLD}{PURPLE}{" ":39}{RESET} ')
else:
    # Se não tem CTPS, apenas mostra os dados coletados usando recursos do dicionário
    print(f'\n{UNDER}{BOLD}{PURPLE}{" ":39} ')
    print(f'{BOLD}{UNDER}{PURPLE}{B_BLACK}{"DADOS CADASTRADOS":^40}{RESET}')
    for chave, valor in cadastro_dict.items():
        print(f'- {chave.replace("_", " ").title()}: {valor}')

print(f'{UNDER}{BOLD}{PURPLE}{" ":39}{RESET} ')
