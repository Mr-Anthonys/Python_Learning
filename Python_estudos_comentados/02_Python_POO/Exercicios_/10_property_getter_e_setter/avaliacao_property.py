# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================


# A classe `Avaliacao` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Avaliacao:
    def __init__(self, nome, diciplina, nota=0):
        self.nome = nome
        self.diciplina = diciplina
        self._nota = nota


    # Atributo Validavél com property
    @property
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def nota(self): # Getter retorna o valor da nota
        return self._nota

    @nota.setter
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def nota(self, valor): # Setter valida a nota se está entre 0 e 10 e atribui o valor p/ o atributo protegido
        if 0 <= valor <= 10: 
            self._nota = valor  
        else: 
            print(f'{valor} NOTA INFALIDA')





    

