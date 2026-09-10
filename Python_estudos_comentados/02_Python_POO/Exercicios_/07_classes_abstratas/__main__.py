# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# from classes_abstratas import * # Importando tudo do arquivo Classes_ex_05

from classes_abstratas import Aluno, Professor, Funcionario # Impotando Classe por Classe.


# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    a1 = Aluno('Gui', 32, 'ADS', 'Turma-A')
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor('Gregory', 44, 'Fisica', 'Mestre')
    p1.dar_aula()


    f1 = Funcionario('Thais', 28, 'CEO', 'Estetica-Calleza')
    f1.bater_ponto()

    a1.estudar()
    p1.estudar()
    f1.estudar()

if __name__ == "__main__":
    main()