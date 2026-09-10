# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from conta_bancaria_encapsulada import ContaBancaria

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    c1 = ContaBancaria(992, "Guilherme", 3000)
    print(c1)

if __name__ == "__main__":
    main()

