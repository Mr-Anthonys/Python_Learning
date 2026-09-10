# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from hashlib import sha256

# A classe `ContaBancaria` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class ContaBancaria():
    """
    Cria uma conta bancária  e permite fazer saques e depósitos.
    """


    # Construtor da classe: é executado quando um novo objeto é criado e inicializa seus atributos.
    def __init__(self, id:int, nome:str, saldo:float=0, chave:str = None):#  Método construtor.
        self._id = id # Protegido (#)
        self._titular = nome # Protegido (#) 
        self.__saldo = saldo # Privado (-)
        if chave == None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        print(f'Conta {self._id} criada com sucesso, saldo atual de R${self.__saldo:,.2f}.')

    # Método que executa o comportamento indicado pelo nome, usando os dados e regras da classe.
    def pede_senha(self) -> str:
        from pwinput import pwinput # Escopo de importação somente dentro do metodo pede_senha
        while True:
            senha = str(pwinput("SENHA: ")).strip()
            if len(senha) >= 6:
                break
            else:
                print(f"Senha inválida, informe pelo menos 6 caracteres.")
        return senha
    # Maneira sem usar o PWINPUT
#region     
        # while True:
        #     senha = str(input(f"SENHA: ")).strip()
        #     if len(senha) >= 6:
        #         break
        #     else:
        #         print(f"Senha inválida, informe pelo menos 6 caracteres.")
        # return senha
#endregion

    # Valida a senha de acordo com a regra definida no exercício.
    def validar_senha(self, chave:str) -> bool:
        entrada_usuario = sha256(chave.encode('utf-8')).hexdigest()
        if entrada_usuario == self.__hash:
            return True
        else:
            return False

    # Define a representação em texto do objeto quando ele é convertido para `str()` ou exibido com `print()`.
    def __str__(self):
        return f'Estado atual da conta {self.__dict__}'

    # Método especial relacionado à forma como o estado do objeto é obtido.
    def __getstate__(self):
        return f'ESTADO: _id = {self._id} ; nome = {self.titular} ; saldo = {self.__saldo}'

    # Realiza a operação `depositar` sobre os dados do objeto, aplicando as regras definidas no exercício.
    def depositar(self, valor):
        self.__saldo = self.__saldo + valor
        print(f'Deposito de \033[32mR${valor:,.2f}\033[0m autorizado na conta {self._id}')
        

    # Realiza a operação `sacar` sobre os dados do objeto, aplicando as regras definidas no exercício.
    def sacar(self, valor:float, chave:str = None):
        valor = abs(valor)

        if chave == None:
            chave = self.pede_senha()

        if self.validar_senha(chave):
            if valor > self.__saldo:
                print(f'Saque de \033[31mR${valor:,.2f}\033[0m NEGADO\nSALDO INSUFICIENTE')
            else:
                self.__saldo = self.__saldo - valor
                print(f'Saque de R${valor:,.2f} Realizado com sucesso.')
        else:
            print(f"Senha não confere, SAQUE NÃO REALIZADO")

