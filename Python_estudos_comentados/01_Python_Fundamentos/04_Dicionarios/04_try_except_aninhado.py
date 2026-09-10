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

#Exercício 93 Try aninhado com while e for + lista para um print VISUAL
#region

#Crie um programa que gerencie o aproveitamento de um jogador. O programa vai ler o NOME, QNT de partidas, QNT de gols (em cada partida).
# Guarde tudo em um dict(), incluindo o total de gols feito durante o campeonato. 


jogador = dict()
jogador_lista = list()
#Bloco de validação do NOME
while True:    
    print(f'{BOLD}{B_BLACK}{CYAN}={RESET}'*40)
    nome = str(input(f'{BOLD}{CYAN}NOME DO JOGADOR:{RESET}').strip().lower())#entrada_str do nome    
    
    if nome.isalpha():#Verificando se é apenas letras
        jogador["nome"] = str(nome)#se for letras, o nome vai para o dict()
        print(f'{BOLD}{B_BLACK}{CYAN}={RESET}'*40)
      
        print(f'NOME "{BOLD}{UNDER}{CYAN}{jogador["nome"].title()}{RESET}", foi cadastrado com sucesso.')
      
        break        
    else:#Se n for apenas letras,avisa !
        
        print(f'{UNDER}{BOLD}{RED}Nome inválido: Inserir apenas letras.{RESET}')



#-Bloco de validação quantidades de partidas.
while True:
    try:
        print(f'{BOLD}{B_BLACK}{CYAN}={RESET}'*40) 
        qnt_partida = int(input(f'{BOLD}{CYAN}{B_BLACK}QUANTIDADES DE PARTIDAS:{RESET} ').strip())
        print(f'{BOLD}{B_BLACK}{CYAN}={RESET}'*40)
      
        jogador["qnt_partidas"] = qnt_partida
        print(f'{BOLD}{CYAN}{qnt_partida}{RESET} Partidas cadastradas.')
        break
    except (ValueError):
        print(f'{BOLD}{UNDER}{RED} Valor inválido, informe apenas números inteiros: ')



#-Bloco de validação quantidade de gols.

for p in range(qnt_partida):# para cada p na qnt de partida
    while True:#laço para verificação
        try:#tente
            print(f'{BOLD}{B_BLACK}{CYAN}={RESET}'*40)
            qnt_gols = int(input(f'{BOLD}{CYAN}{B_BLACK}QUANTIDADE DE GOLS NA {p+1}º PARTIDA:{RESET} ').strip()) 
            print(f'{BOLD}{B_BLACK}{CYAN}={RESET}'*40)                      
            jogador[f"partida_{p+1}"] = qnt_gols
            print(f'{BOLD}{B_BLACK}{CYAN}{p+1}º Partida cadastrada com sucesso.{RESET}')   
            jogador_lista.append(qnt_gols)
            #se tydo acima deu certo saia do laço infinito e volte para o FOR, para continuar as partidas
            break   
        except(ValueError):
            print(f'{BOLD}{UNDER}{RED}QUANTIDADE DE GOLS INVÁLIDA!')

jogador["total_gols"] = sum(jogador_lista)

#-Resultado

print(f'{BOLD}{UNDER}{B_BLACK}{CYAN} {RESET}'*40)
print(f'{"RESULTADO":^40}')
print(f'{BOLD}{UNDER}{B_BLACK}{CYAN} {RESET}'*40)

for k, v in jogador.items():
    
    print(f'- {BOLD}{CYAN}{k.replace("_", " ").title()}{RESET}: {BOLD}{UNDER}{GREEN}{v}{RESET}') 

print(f'O jogador{BOLD}{GREEN} {jogador["nome"].title()}{RESET}. jogou {qnt_partida} partidas.')

#Usando uma lista para uma saida visualmente melhor !!
for i, gols in enumerate(jogador_lista):
    print(f'   => Na {i+1}º partida, fez {BOLD}{GREEN}{gols}{RESET} gols.')

print(f'Foi um total de {BOLD}{GREEN}{jogador["total_gols"]}{RESET} gols.')
   
