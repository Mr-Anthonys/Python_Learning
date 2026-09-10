# ============================================================
# Estudos da biblioteca Rich
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# from rich import print
# from rich.panel import Panel

# caixa = Panel('[bold black]Painel de exemplo[/]',title='Mensagem', style="blue", width=25)

# print(caixa)



# print(Panel("Conteúdo importante", title="Aviso", border_style="red"))
# print(Panel.fit("Ajusta ao tamanho do texto"))


from rich.columns import Columns
from rich import print

itens = [f"Item {i}" for i in range(20)]
print(Columns(itens))




# from rich.panel import Panel
# from rich import print

# class Churrasco:
#     def __init__(self, qnt_pessoas, ):
#         self.qnt_pessoas = qnt_pessoas

    # Metodos

    # def Analisar(self):

    #     self.v_pessoa = 32.96
    #     self.kilos = self.qnt_pessoas * 0.4
    #     self.total = self.v_pessoa * self.qnt_pessoas


    #     box_msg = Panel.fit(

    #         f'Analisando churrasco com [yellow]{self.qnt_pessoas}[/] pessoas.\n'
    #         f'Considerando 400g de consumo para cada pessoa.\n'
    #         f'Recomendo comprar [bold red]{self.kilos:,.2f}Kg[/] de carne.\n'
    #         f'O custo total será de [bold green]R$:{self.total:,.2f}[/]\n'
    #         f'Cada pessoa pagara [bold yellow]R$:{self.v_pessoa:,.2f}[/]\n',
    #         title='< CHURRAS >',
    #         style= 'cyan on black'
    #      )



    #     print(box_msg)





# c = Churrasco(6)
# c.Analisar()