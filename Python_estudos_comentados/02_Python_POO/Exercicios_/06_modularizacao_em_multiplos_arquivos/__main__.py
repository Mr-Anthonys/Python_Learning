# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# from Classes_ex_05 import * # Importando tudo do arquivo Classes_ex_05

from aluno import Aluno
from funcionario import Funcionario
from professor import Professor

# Declaro uma função do python main()
# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():

    # Coloco td o code dentro dessa função
    a1 = Aluno('Gui', 32, 'ADS', 'Turma-A')
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor('Gregory', 44, 'Fisica', 'Mestre')
    p1.dar_aula()


    f1 = Funcionario('Thais', 28, 'CEO', 'Estetica-Calleza')
    f1.bater_ponto()

# Verifico se o nome do arquivo é __main__ (arquivo do programa principal)
if __name__ == '__main__':

    main() # Executo o code q coloquei dentro da função main

