# ============================================================
# Exercício de dicionários
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#-Exercicio 6.
#Crie um programa que leia o NOME,SEXO e IDADE de várias pessoas.
#Guardando os dados em um dicionário e todos dicionários em uma lista.
#No fimal mostre:
#A) Qntas pessoas cadastradas.
#B) A média de idade.
#C) Uma lista com muheres.
#D) lista com idade acima da média

pessoas = list()
lista_mulheres = list()

while True:
    #Dicionário vazio sendo criado dentro do laço.
    dict_temp = dict()

    #- Bloco de verificação do NOME.
    while True:
        print('-='*30)
        nome = str(input('NOME: ').strip())

        #se nome sem espaços (replace) é apenas letras:
        if nome.replace(' ','').isalpha():

            #O nome é adicionádo ao dicionário.
            dict_temp["nome"] = nome.title()
            print('-='*30)
            print(f'O nome --> "{dict_temp["nome"]}" Cadastrado com sucesso. ')

            
            break#fim do laço de verificação
        #se ñ for apenas letras.
        else:
            print('-='*30)
            print(f'"NOME" iválido, informe apenas letras.')

    #- Bloco de verificação do SEXO.
    while True:
        print('-='*30)
        sexo = str(input(f'SEXO: ').strip().upper()[0])#sem espaços, e pegando a 1º letra em maiusculo.
        if sexo in 'MF':
            dict_temp["sexo"] = sexo
            print('-='*30)
            print(f'Sexo {dict_temp["sexo"]} cadastrado com sucesso.')
            if sexo == 'F':
                lista_mulheres.append(dict_temp["nome"])
            break
        else:
            print('-='*30)
            print(f'"SEXO" inválido, informe [M/F].')

    #- Bloco de verificação da IDADE.
    while True:
        try:
            print('-='*30)
            idade = int(input('IDADE: ').strip())
            dict_temp["idade"] = idade
            print('-='*30)
            print(f'Idade {dict_temp["idade"]}, cadastrado com sucesso.')
            pessoas.append(dict_temp.copy())
            break
        except (ValueError):
            print('-='*30)
            print(f'Idade inválida, informe apenas números inteiros.')

    #- Bloco de verificação da RESPOSTA.
    while True:
        print('-='*30)
        r = str(input('CONTINUAR? [S/N]: ').strip().upper()[0])
        if r in 'SN':#Aqui verifica se digitou certo [S ou N]
           break#para a verificação (como a resposta n foi == N) o if la de baixo n roda e continua o cadastro
    else:# Esse else está alinhado com o while True: da validação e não com o IF
        print(f'Resposta inválida, informe apenas [S/N].')

    if r == 'N':
        print(f'Encerrando cadastro.')
        print('-='*30)

        break#Esse para o 1 laço.
          
#- Resultado
print(f'Quantidade de pessoas cadastradas ---> {len(pessoas)} ')
print('-='*30)
# - Media da idade
lista_total_idade = []

for c, v in enumerate(pessoas):
    lista_total_idade.append(pessoas[c]["idade"])

media = sum(lista_total_idade) / len(lista_total_idade)
print(f'A média de todas as idade foi de: {media:.2f}')
print('-='*30)
print(f'Lista com as mulheres: {lista_mulheres}')

#para cada dicionário em pessoas (p aqui vale 1 dicionário completo)
for p in pessoas:
    if p["idade"] > media:#se o p["idade"] vai procurar o valor da chave ["idade"]
        #Printamos na tela o nome e a idade direto!
        print(f'   -> {p["nome"]} tem {p["idade"]} anos.')#Podemos imprimir na tela pelas keys do dicionario.




    
        
      



    







