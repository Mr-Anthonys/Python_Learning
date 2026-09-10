# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Usuario vai digitar o comando do interative help do python, e o manual aparece, se digitar fim encerra

from time import sleep
# Exibe informações de ajuda sobre os comandos ou recursos do exercício.
def ajuda(com):
    titulo(f'Acessando o manual do comando "{com}"')
    sleep(1)
    help(com)


# Formata/exibe um título para organizar a saída do programa.
def titulo(msg, cor=0):
    tam = len(msg)+6
    print('~'* tam)
    print(f'{msg:^{tam}}')
    print('~' * tam)


# programa principal
while True:
    titulo('SISTEMA DE AJUDA')
    comando = str(input('Função ou Bibliotéca > '))
    sleep(1)
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO.')
