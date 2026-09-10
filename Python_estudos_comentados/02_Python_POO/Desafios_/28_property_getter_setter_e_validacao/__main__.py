# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from Termostato import *
from rich import print, inspect
# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    t = Termostato()
    print(f'Temperatura atual = {t.temperatura}')

    
    print(f'Temperatura atual é {t.temperatura}')
    print(f'Temperatura formatada é = {t.ftemperatura}')  


if __name__ == "__main__":
    main()


