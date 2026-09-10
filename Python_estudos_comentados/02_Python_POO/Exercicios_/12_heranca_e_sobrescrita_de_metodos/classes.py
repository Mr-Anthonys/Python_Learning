# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Outro exemplo de POLIMORFISMO DE INCLUSÃO (OVERRIDE/SOBREESCRITO/SUBTYPING)

# Uma Classe mãe com 
# Um atributo "NOME"
# Dois métodos ("FAZER PUDIM / FRITAR COXINHA")

# A classe `Mae` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Mae:
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome


    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def fazer_pudim(self):
        print(f'{self.nome} faz "PUDIM" com leite condensado.')

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def fritar_coxinha(self):
        print(f'{self.nome} frita "COXINHA" com óleo de soja.')



 # --------------------------------------------------------------------
 # Sub-Classes (derivadas / filhas )
 # --------------------------------------------------------------------


 # Filha vai herdar o método fritar_coxinha() E vai SUB-ESCREVER / OVER-RIDE o método de fazer_pudim()
# A classe `Filha` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Filha(Mae):
    # Sub-escrevendo o método de fazer PUDIM.
    def fazer_pudim(self):
        print(f'{self.nome} faz "PUDIM" com nutela e ninho.') 




# Filho vai herdar o método fazer_pudim() E vai SUB-ESCREVER / OVER-RIDE o método de fritar_coxinha()
# A classe `Filho` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Filho(Mae):    
    # Sub-escrevendo o método de fritar COXINHA
    def fritar_coxinha(self):
        print(f'{self.nome} frita "COXINHA" na Air-Fryer, sem óleo.')


# ---------------------------------------------------------------------------------------------------------
# FILHA
# ---------------------------------------------------------------------------------------------------------
# Caso a "FILHA" chame o método de fritar_coxinha()
# Saída: -> f'{self.nome} frita "COXINHA" com óleo de soja.' (igual a saída da MÃE)

# Caso a "FILHA" chame o método de fazer_pudim()
# Saída: -> f'{self.nome} faz "PUDIM" com nutela e ninho.' (método especializado, diferente da MÃE)




# ---------------------------------------------------------------------------------------------------------
# FILHO
# ---------------------------------------------------------------------------------------------------------
#Caso a "FILHO" chame o método de fazer_pudim() 
# Saída: ->  f'{self.nome} faz "PUDIM" com leite consensado e calda.' (igual a saída da MÃE)

# Caso a "FILHO" chame o método de fritar_coxinha()
# Saída: -> f'{self.nome} frita "COXINHA" na Air-Fryer, sem óleo.' (método especializado, diferente da MÃE)

