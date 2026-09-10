# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from Alunos import Pessoa, Aluno

# Função principal: organiza a execução do programa e chama as partes necessárias para realizar o exercício.
def main():
    a = Aluno("Gui", 1994, "DEV")
    b = Aluno("Thais", 1998, "ADS")

    a.add_curso("MODA")
    a.curso = "MODA"
    a.nascimento = 2022
    

    print(b.cursos_oficiais)
    print(a.idade)
    print(a.__dict__)
    print(b.__dict__)
    

if __name__ == "__main__":
    main()