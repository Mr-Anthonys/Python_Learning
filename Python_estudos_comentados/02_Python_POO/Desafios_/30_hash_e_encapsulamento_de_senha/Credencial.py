# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
from hashlib import sha256
from rich import print


# A classe `Credencial` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Credencial:

    # Método construtor sem receber paramêtros, e com apenas 1 atributo privado = __hash
    def __init__(self):
        self.__hash = None


    # Aatributo personalizável
    @property
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def senha(self): # Caso queira visualisar a senha
        return self.__hash # será exibido o HASH. conteúdo criptografado.

    @senha.setter
    # Método de acesso/alteração de um atributo; neste exercício, ele ajuda a controlar como esse dado é lido ou modificado.
    def senha(self, chave):
        if len(chave) > 0: # se a cahve informada não estiver vazia -> " "
            self.__hash = sha256(chave.encode('utf-8')).hexdigest() # o atributo self.__hash 
                                                                    # vai receber a chave encodada em 'utf-8' 
                                                                    # e exibida em hexadecimal
        else:
            raise PermissionError ("[red]SENHA INCORRETA ![/]")

        
    # Valida a senha de acordo com a regra definida no exercício.
    def validar_senha(self, chave):


        entrada_usuario = sha256(chave.encode('utf-8')).hexdigest() # Criptografando a entrada do usuario em hash(da mesma forma q o atributo __hash)
        if entrada_usuario == self.__hash:                          # Verificando se as 2 Hash são iguais.
            print("Senha válida, bate com a hash salva no atrib.")
            return True                                             # Retorna verdadeiro (um print apenas pra informar)                                                        
        else:
            print(f"Senha inválida, não bate com a hash salva do atrib")
            return False                                             # Caso contrario retorna falso.