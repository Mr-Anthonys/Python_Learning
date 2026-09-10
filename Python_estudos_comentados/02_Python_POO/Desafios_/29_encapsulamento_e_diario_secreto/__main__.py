# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from Diario_secreto import *
from rich import print, inspect

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    d = Diario("abc")

    d.escrever("Olá, mundo")
    d.escrever("Estamos aprendendo POO")
    d.escrever("Python é incrivél !!")

    try:
        d.ler("abc")
    except PermissionError as erro:
        print(f"{erro}")


    try:
        d.alterar_senha("abc", "Testenovasenha1234")

    except PermissionError as erro:
        print(f"{erro}")

    #inspect(d, private=True, methods=True)    
if __name__ == "__main__":
    main()