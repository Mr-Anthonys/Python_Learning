# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from Fretes import *
# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    dist = 9.9
    entrega = Drone(dist)
    entrega.calc_frete()
    print(f"Frete de {type(entrega).__name__} em {dist}Km  --> {entrega.calc_frete()}")

    
if __name__ == "__main__":
    main()