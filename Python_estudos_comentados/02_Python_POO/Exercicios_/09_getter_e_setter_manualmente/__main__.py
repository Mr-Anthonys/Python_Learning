# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from avaliacao_getter_setter import Avaliacao
from rich import print, inspect


    # _nota -> seria a nota protegida, não sendo possível alterar esse atributo estando fora da classe.
    # exemplo av1.nota = -87  nesse caso aqui o objeto criado iria alterar a nota se ñ estivesse protegida
    # av1.nota = -87 o python vai criar um atributo chamado nota = -87 porem o atributo protegido (_nota) vai continuar com o 9.5

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    av1 = Avaliacao("Gui", "Fisica")
    #av1.nota = -87
    print(f"{av1.nome} tirou {av1.get_nota()} ná máteria {av1.diciplina}")
    av1.set_nota(7.5)
    inspect(av1, private= True)



   


if __name__ == "__main__":
    main()