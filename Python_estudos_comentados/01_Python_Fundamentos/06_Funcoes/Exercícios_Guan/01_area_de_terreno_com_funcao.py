# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#-Exercicio 1
#-Faça um programa que tenha uma função chamada área()
#-Que receba as dimensões de um terreno retangular(LARGURA e COMPRIMENTO)
#-Mostre a área do terreno.

#-Declarando a função
def área(l, c):
    a = (l * c)
    print(f'Com {l}m  X  {c}m  Temos um terreno de {a}m².')



#- Programa principal
print('_'*30)
print(f'{"Terreno":^30}')
print('_'*30)



#-Bloco de verificação dos parâmetros.
while True:
    #- Verifique se o input é valido
    #- .replace(',' . '.') Se caso a entrada for ex: 9,5 vai trocar p/ 9.5 (Aceito pelo float)
    try:
        larg = float(input('LARGURA: ').strip().replace(',' , '.'))
        comp = float(input('COMPRIMENTO: ').strip().replace(',' , '.')) 

        #- Se tudo deu certo, pare o laço de verificação
        break  
    

    #- Se o TRY n deu certo, verifique os erros Type e Value e avise o usuário.
    except(TypeError),(ValueError):
        print(f'Informe apenas valores númericos.')


#-Chamando as funções com os parâmetros certos
área(larg,comp)

