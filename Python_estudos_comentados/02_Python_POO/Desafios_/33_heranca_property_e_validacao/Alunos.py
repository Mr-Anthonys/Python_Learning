# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from abc import ABC, abstractmethod
from datetime import date

# A classe `Pessoa` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Pessoa(ABC):
    def __init__(self, nome:str, nasc:int):
        self._nome = nome
        self._nascimento = None
        self.nascimento = nasc



    @property
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def nascimento(self, ano:int):
        if 1900 <= ano <= date.today().year:
            self._nascimento = ano
        else:
            raise ValueError(f"ANO -> {ano} é IVÁLIDO")


    @property
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def idade(self):
        return date.today().year - self._nascimento

    @idade.setter
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def idade(self, valor):
        raise PermissionError ("Para alterar a idade, precisa mudar o ANO DE NASCIMENTO.")



# A classe `Aluno` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Aluno(Pessoa):
    cursos_oficiais = ["ADM", "ADS", "FISÍCA", "MEDICINA", "DEV"]

    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, nome:str, nascimento:int, curso:str):
        super().__init__(nome, nascimento)
        self._curso = None

        self.curso = curso


    @property
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def curso(self):
        return self._curso

    @curso.setter
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def curso(self, curso):
        if curso in Aluno.cursos_oficiais:
            self._curso = curso
        else:
            self._curso = None
            raise ValueError(f"O Curso {curso} não está na lista de cursos oficiais.")
            

    # Adiciona uma informação à estrutura de dados usada pelo objeto ou pelo exercício.
    def add_curso(self, curso:str):
        curso = curso.strip().upper()
        if curso in Aluno.cursos_oficiais:
            raise PermissionError(f"O curso {curso} já está na lista de cursos oficiais.")

        elif 3 <= len(curso) <= 7:
            Aluno.cursos_oficiais.append(curso)
        else:
            raise PermissionError(f"Curso {curso} não atende os requisitos para ser adicionado.")

        
