# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# A classe `TermostatoGuana` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class TermostatoGuana:
    def __init__(self):
        self.__temperatura = 24


    @property
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f"TEMPERATURA DE {valor}{chr(176)}C É INVÁLIDA ! ")

        if valor < 16:
            self.__temperatura = 16 #Travou a temp em 16

        elif valor > 30:
            self.__temperatura = 30 # Travou em 30

        else:
            self.__temperatura = valor

    @property
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def ftemperatura(self):
        return f"{self.__temperatura} ºC"


