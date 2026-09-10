# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

# A classe `Retangulo` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Retangulo:
    def __init__(self, base = 1, altura = 1):
        self._base = None
        self._altura = None
        self._area = None
        

        # Atributos validados com o property, esses são o base/altura do contrutor.
        self.base = base 
        self.altura = altura



    # property da base
    @property
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def base(self):
        return self._base

    @base.setter
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def base(self, valor):
        # SE VALOR NÃO FOR FLOAT OU INT -> RAISE ERROR
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError("O valor deve ser um número.")
        # SE VALOR FOR MENOR QUE ZERO -> RAISE ERROR
        if valor < 0:
            raise ValueError("Valor inválido para a BASE !")
        else: # TUDO OK, ACEITA O VALOR PARA O ATRIBUTO PROTEGIDO _BASE
            self._base = valor

        

    # property da altura    
    @property
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def altura(self):
        return self._altura

    @altura.setter
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def altura(self, valor):
        if not isinstance(valor, float) and not isinstance(valor, int):
            raise TypeError ("O valor deve ser um número.")
        
        if valor < 0:
            raise ValueError("Valor inválido para ALTURA !")
        else:
            self._altura = valor

    # property da area
    @property
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def area(self):
        self._area = self._base * self._altura
        return self._area

    @area.setter
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def area(self):
        raise PermissionError("Área não pode ser configurada desse jeito.")

    # property da medidas
    @property
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def medidas(self):
        return f"BASE = {self.base}\nALTURA = {self.altura}\nÁREA = {self.area}"

    @medidas.setter
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def medidas(self, valores:list):
        # Verificando se é uma lista
        if not isinstance(valores, list):
            raise TypeError("VALORES devem ser passados em forma de lista")
        
        # Verificando se foi passadi 2 valores.
        if len(valores) != 2:
            raise SyntaxError(f"Informe uma lista com 2 VALORES.")

        # Verificando 1º valor da lista se é float ou int ! 
        if isinstance(valores[0], float) or isinstance(valores[0], int):
            self.base = valores[0]
        else:
            raise TypeError("A BASE deve ser um número.")

        if isinstance(valores[1], float) or isinstance(valores[1], int):
            self.altura = valores[1]
        else:
            raise TypeError("A ALTURA deve ser um número.")
            

        

    