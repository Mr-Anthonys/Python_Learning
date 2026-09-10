# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Classe Termostato
# Min = 16º , Max = 30º
# Liga em 24º
# Pula de meio em meio. 16,5 -> 17 -> 17,5 . . .
# Atributos, __temperatura, @temperatura, @ftemperatura (retorna formatado 25ºCelsios)

from rich import print, inspect

# A classe `Termostato` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Termostato:
    def __init__(self):
        self.__temperatura = 24


    @property # Getter da temperatura
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def temperatura(self):
        return self.__temperatura 

    @temperatura.setter
    
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def temperatura(self, temp):
        while True:
            if 16 <= temp <= 30 and (temp % 1 == 0.0 or temp % 1 == 0.5):
                self.__temperatura = temp
                break
            else:
                try:
                    temp = float(input(f"Valor {temp} inválido !\nInforme temperaturas entre 16 até 30.\nEx:[16 ou 16.5]: ").strip().replace(',','.'))            

                except (ValueError , TypeError):
                    print("Valor informado inválido")
                
            


    @property # Getter da ftemperatura
    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def ftemperatura(self):
        return f"{self.__temperatura} ºC"
        




        