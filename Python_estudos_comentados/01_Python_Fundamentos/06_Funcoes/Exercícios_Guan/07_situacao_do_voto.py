# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# função voto()
#Receba como param: o ano de nascimento
#retorne um valor literal indicando se a pessoa:
# tem o voto negado opcional ou obrigatorio
#opcional (60)a e negado (<16)
#ano atual 2026

# Determina a situação do voto de acordo com a idade informada.
def voto(ano_nsc):
    """Recebe o ano de nascimento e exibe a situação de voto
    Arg*: 
        ano_nsc=0
    Return:
        Situação de VOTO
    """

    idade = (2026-ano_nsc)    
    if idade >= 16 and idade <= 59:
        return (f'Com {idade} anos, "O VOTO OBRIGATÓRIO !"')
    elif idade < 16:
            return (f'Com {idade} anos, "O VOTO É NEGADO! "')
    elif idade > 59:
        return (f'Com {idade} anos, "O VOTO É OPICIONAL"')
    
    
#programa principal
ano = int(input(f'ANO DE NASCIMENTO: '))
resultado = voto(ano) # Resultado recebe a função VOTO com a entrada do input como parametro.

print(resultado)




