# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#-Exercicio 2
#-Faça um programa que tenha uma função chamada ESCREVA()
#-Que receba qualquer parâmetro e mostre uma mensagem com tamanho adaptável.
# EX--> escreve('Olá,Mundo!')
# SAÍDA -->
#       ~~~~~~~~~~
#       Olá Mundo!
#       ~~~~~~~~~~

# Executa a escrita solicitada pelo exercício.
def escreva(txt):
    tam_linha = len(txt)    
    
    print('~'*(tam_linha+4))
    print(f'{txt:^{tam_linha+4}}')
    print('~'*(tam_linha+4))


#- Programa Principal

txt = str(input(f'Informe seu texto para mensagem com tamanho adaptável.\n--->  '))
escreva(txt)





