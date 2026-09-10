# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from avaliacao_property import Avaliacao
from rich import print, inspect


    
# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    av1 = Avaliacao("Gui", "Fisica")
    av1.nota = -99
    print(f"{av1.nome} tirou {av1.nota} ná máteria {av1.diciplina}")
    
    inspect(av1, private= True)



   


if __name__ == "__main__":
    main()