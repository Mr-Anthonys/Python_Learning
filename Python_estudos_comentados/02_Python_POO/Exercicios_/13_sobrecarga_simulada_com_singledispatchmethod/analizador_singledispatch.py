# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# POLIMORFISMO DE SOBRE-CARGA DE MÉTODOS 
# Diversos métodos com o MESMO NOME, porém com assinaturas diferentes (paramêtros). Executando funcionalidades diferentes.

# OBS: Python não consegue fazer a sobrecarga de métodos naturalmente, é necessário fazer um "singledispatch"
# Sendo necessário importar uma LIB interna -> "FUNCTOOLS", singledispatchmethod

# Importamos o decorator que vai permitir "simular" a sobrecarga de métodos
from functools import singledispatchmethod

# A classe `Analizador` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Analizador:

    # @singledispatchmethod transforma "analisar" no método principal (o "despachante")
    # Ele é quem vai decidir, na hora da chamada, qual versão do método deve rodar
    @singledispatchmethod
    # Executa a análise principal proposta pelo exercício.
    def analisar(self, valor):
        # Esse é o método PADRÃO (fallback)
        # Roda quando o tipo do "valor" não bate com NENHUM tipo registrado abaixo
        print(f'Não foi possível analisar o valor "{valor}".')


    # @analisar.register registra uma nova "versão" do método analisar,
    # associada a um tipo específico de dado (definido pela anotação de tipo)
    # O nome do método é "_" porque ele nunca é chamado diretamente,
    # só é acessado através de "analisar()" -> por isso o nome não importa por convensão usa o -> _
    @analisar.register
    # Função/método responsável pela operação indicada pelo nome dentro deste exercício.
    def _(self, valor:int):
        # Essa versão roda quando "valor" for do tipo INT
        print(f'{valor} é um número INTEIRO.')

    @analisar.register
    # Função/método responsável pela operação indicada pelo nome dentro deste exercício.
    def _(self, valor:str):
        # Essa versão roda quando "valor" for do tipo STR
        print(f'{valor} é uma cadeia de CARACTERES.')

    @analisar.register
    # Função/método responsável pela operação indicada pelo nome dentro deste exercício.
    def _(self, valor:list):
        # Essa versão roda quando "valor" for do tipo LIST
        print(f"{valor} é uma LISTA.")

    @analisar.register
    # Função/método responsável pela operação indicada pelo nome dentro deste exercício.
    def _(self, valor:tuple):
        # Essa versão roda quando "valor" for do tipo TUPLE
        print(f"{valor} é uma TUPLA ")

    @analisar.register
    # Função/método responsável pela operação indicada pelo nome dentro deste exercício.
    def _(self, valor:dict):
        # Essa versão roda quando "valor" for do tipo DICT
        print(f"{valor} é um DICT ")


# A ideia central pra fixar: 
# analisar() é a porta de entrada única.
# O Python, por baixo dos panos, olha o tipo do argumento(parametro) e redireciona pra função registrada certa.
# Como se fosse um "switch" automático baseado em tipo.