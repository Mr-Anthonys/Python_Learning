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
# RESET  = "\033[0m"
# BOLD   = "\033[1m"
# UNDER  = "\033[4m"

# # Cores de Texto
# BLACK  = "\033[30m"
# BLUE   = "\033[34m"
# PURPLE = "\033[35m"
# RED    = "\033[31m"
# GREEN  = "\033[32m"
# YELLOW = "\033[33m"
# CYAN   = "\033[36m"

# #Cores de Fundo
# B_RED   = "\033[41m"
# B_BLACK = "\033[40m"
# B_BLUE  = "\033[44m"
# B_WHITE = "\033[47m"

#endregion


#Exercício 91 itemgetter
#region

#Crie um programa onde 4 jogadores joguem um DADO e tenham resultados aleatórios.
#Guarde esses resultados em um dict()
#No final coloque o dict() em ordem, sabendo que o vencedor tirou o maior número no dado.

#-Importando as bibliotecas
# from random import randint
# from time import sleep


# jogadores_dict = {}
# numeros_sorteados = []
# numero = 0
# print(f'{BOLD}{B_WHITE}={RESET}'*50)
# print(f'{BOLD}{"DADOS":^50}{RESET}')
# print(f'{BOLD}{B_WHITE}={RESET}'*50)


# for j in range(1, 5):
#     numero = (randint(1,6))    
#     jogadores_dict[f"jogador_{j}"] = numero
#     print(f'O {j}º Jogador sorteou o Nº: {numero}')
#     numeros_sorteados.append(numero)
#     sleep(0.75)

# numeros_sorteados.sort(reverse=True)

# print(f'{BOLD}{B_WHITE}={RESET}'*50)
# print(f'{BOLD}{"RANKING":^50}{RESET}')
# print(f'{BOLD}{B_WHITE}={RESET}'*50)

# print(f'')


#- Resolução Guanabara_itemgueter ?
from time import sleep
from random import randint

from operator import itemgetter # !!!!!!!!!! ?


jogo = {"jogador1" : randint(1,6),
        "jogador2" : randint(1,6),
        "jogador3" : randint(1,6),
        "jogador4" : randint(1,6),
        "jogador5" : randint(1,6)}

ranking = []

print(f'Valores Sorteados:')

for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print(ranking)

for i, v in enumerate(ranking):
    print(f'{i+1}º-Lugar: {v[0]} com {v[1]}.')
    sleep(1)
