# ============================================================
# Desafio de POO
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# - Crie a classe Churrasco, onde seja possível informar 
# Quantas pessoas vão participar.
# Quanto de carne deve ser comprado.
# O custo total do churrasco.
# Preço total por pessoa.
# Considere:
# Consumo padrão 400g por pessoa
# Preço: R$ 82,40/Kg


from rich.panel import Panel
from rich import print

# A classe `Churrasco` representa uma entidade/estrutura do exercício e reúne dados e comportamentos relacionados.
class Churrasco:
    def __init__(self, qnt_pessoas, ):
        self.qnt_pessoas = qnt_pessoas

    # Metodos

    # Função/método responsável pela operação indicada pelo nome dentro deste exercício.
    def Analisar(self):
        
        self.v_pessoa = 32.96
        self.kilos = self.qnt_pessoas * 0.4
        self.total = self.v_pessoa * self.qnt_pessoas

        
        box_msg = Panel.fit(

            f'Analisando churrasco com [yellow]{self.qnt_pessoas}[/] pessoas.\n'
            f'Considerando 400g de consumo para cada pessoa.\n'
            f'Recomendo comprar [bold red]{self.kilos:,.2f}Kg[/] de carne.\n'
            f'O custo total do churrasco será de [bold green]R$:{self.total:,.2f}[/]\n'
            f'Cada pessoa pagara [bold yellow]R$:{self.v_pessoa:,.2f}[/]\n',
            title='< CHURRAS >', 
            style= 'cyan on black'
         )
        print(box_msg)
    
        



c = Churrasco(6)
c.Analisar()





        