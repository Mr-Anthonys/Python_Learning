# ============================================================
# Exercício de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# A classe `ContaBancaria` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class ContaBancaria():
    """
    Cria uma conta bancária  e permite fazer saques e depósitos.
    """


    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, id, nome, saldo=0):#  Método construtor.
        self.id = id
        self.titular = nome 
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso, saldo atual de R${self.saldo:,.2f}.')

    # Define a representação em texto do objeto quando ele é convertido para `str()` ou exibido com `print()`.
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo.'

    # Método especial relacionado à forma como o estado do objeto é obtido.
    def __getstate__(self):
        return f'ESTADO: id = {self.id} ; nome = {self.titular} ; saldo = {self.saldo}'

    # Realiza a operação `depositar` sobre os dados do objeto, aplicando as regras definidas no exercício.
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print(f'Deposito de \033[32mR${valor:,.2f}\033[0m autorizado na conta {self.id}')
        

    # Realiza a operação `sacar` sobre os dados do objeto, aplicando as regras definidas no exercício.
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque de \033[31mR${valor:,.2f}\033[0m NEGADO\nSALDO INSUFICIENTE')
        else:
            self.saldo = self.saldo - valor
            print(f'Saque de R${valor:,.2f} Realizado com sucesso.')


# Objetos
conta_um = ContaBancaria(666, 'Guilherme', 2500)

conta_um.sacar(100)#Saque de 500
conta_um.depositar(1000) # deposito de 1k
print(conta_um)
print(conta_um.__getstate__())

