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

 # MÉTODOS ACESSORES
    # Método de leitura: retorna um valor armazenado no objeto.
    def get_nota(self): # Método Getter
        return self._nota

    def set_nota(self, valor): # Método Setter (Geralmente o setter precisa de uma validação)
        if 0 <= valor <= 10: # Se o valor estiver entre 0 e 10
            self._nota = valor # modifique o valor
        else: # se não estiver entre 0 e 10 (validação pra notas erradas ou negativas)
            print(f'{valor} NOTA INVALIDA')


    

