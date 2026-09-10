# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================


# A classe `Diario` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Diario:
    def __init__(self, senha = "123"):
        self.__segredos = []
        self.__senha = senha.strip()


    # Executa uma ação específica do objeto conforme a proposta do exercício.
    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0: # Se a msg for str, e houver msg (ter algum valor informado) len maior q 0 
            self.__segredos.append(msg.strip())

    
    # Executa uma ação específica do objeto conforme a proposta do exercício.
    def ler(self, senha = None):
        if senha == self.__senha:
            print(f"DIÁRIO DESBLOQUEADO")
            for i, msg in enumerate(self.__segredos):
                print(f"{i+1}º Menssagem -> {msg}")
        else:
            raise PermissionError("ACESSO NEGADO\nSenha inválida")
        
             
    # Executa uma ação específica do objeto conforme a proposta do exercício.
    def alterar_senha(self, senha_antiga, senha_nova):
        if senha_antiga != self.__senha:
            raise PermissionError ("Senha antiga incorreta. não foi possivel alterar a senha.")

        if isinstance(senha_nova, str) and len(senha_nova.strip()) > 0:
            self.__senha = senha_nova.strip()
            print(f"Senha Atualizada com sucesso ! ")
        else:
            raise ValueError ("Erro, Senha nova inválida")


    




        

