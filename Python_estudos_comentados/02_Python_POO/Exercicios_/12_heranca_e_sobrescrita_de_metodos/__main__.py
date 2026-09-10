# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from classes import *

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():

    pessoa_1 = Mae("Maria Valderlene")
    pessoa_2 = Filha("Thais dos Santos")
    pessoa_3 = Filho("Guilherme Roger")

    pessoa_1.fazer_pudim()
    pessoa_1.fritar_coxinha()

    pessoa_2.fazer_pudim()
    pessoa_2.fritar_coxinha()

    pessoa_3.fazer_pudim()
    pessoa_3.fritar_coxinha()

    

if __name__ == "__main__":
    main()