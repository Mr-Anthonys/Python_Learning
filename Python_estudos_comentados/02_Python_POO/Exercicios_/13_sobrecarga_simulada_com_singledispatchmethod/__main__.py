# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from analizador_singledispatch import Analizador

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():

    # Testando na prática:
    obj = Analizador()
    
    obj.analisar(10)          # -> cai na versão "int"
    obj.analisar("Python")    # -> cai na versão "str"
    obj.analisar([1, 2, 3])   # -> cai na versão "list"
    obj.analisar((1, 2))      # -> cai na versão "tuple"
    obj.analisar({"a": 1})    # -> cai na versão "dict"
    obj.analisar(3.14)        # -> nenhum tipo bate, cai no método PADRÃO (fallback)

if __name__ == "__main__":
    main()