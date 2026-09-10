# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from Funcionarios import Horista
from rich import print, inspect


# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    empregado_pj = Horista('Guilherme', 28, 96)
    print(empregado_pj.calcular_salario())


if __name__ == "__main__":
    main()