# ============================================================
# Exercício de dicionários
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#🐍 Snippet Pronto para Python
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

#Leia o nome e a média do aluno guardando também a situação do aluno (APROVAO/REPROVADO) em um dict() no fina mostre as informações

aluno = dict()
while True:
    try:    
        aluno["nome"] = str(input(f'{BOLD}NOME:{RESET} '))    
        aluno["media"] = float(input(f'Informe a média de {aluno["nome"].title()}: '))
        if aluno["media"] <= 6 :
            aluno["situ"] = 'Reprovado'
        else:
            aluno["situ"] = 'Aprovado'
    except: 
        print(f'Informação inválida.')
    else:
        print(f'Valores adicionados com sucesso.')
        break
print(f'O aluno {aluno["nome"].title()} Teve uma média de {aluno["media"]:.1f} e sua situação é {aluno["situ"].upper()}')
