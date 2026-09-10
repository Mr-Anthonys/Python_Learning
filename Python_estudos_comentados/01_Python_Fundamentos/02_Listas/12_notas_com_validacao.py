# ============================================================
# Exercício de listas
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercicio 8. 
# region
# Sistema de Notas com Validação:
#Crie um programa que use um laço while para pedir notas de alunos (de 0.0 a 10.0).
#O programa só deve parar de pedir notas quando o usuário digitar -1.
#Guarde as notas válidas em uma lista e, no final, mostre:
#A) Quantas notas foram digitadas.
#B) A média da turma.
#C) Quantos alunos ficaram acima da média 7.0.

lista_notas = []
lista_media = []
print('='*40)
print(f'{'SISTEMAS DE NOTAS':^40}')

while True:
     #Entrada das notas e confição de parada
    print('='*40)
    print('INFORME NOTAS DE (0.0 a 10.0) ou (-1) para finalizar.')
    entrada_notas_str = input('NOTA: ').strip().replace(',' , '.')#Trocando ',' para '.' (se houver)
    
     #Verificando se a resposta é a condição de parada (ainda em STR)
    if entrada_notas_str == '-1':
        print('Finalizando o SISTEMA')
        break
    
    #Convertendo a entrada STR em apenas numeros sem ponto
    notas_semponto = entrada_notas_str.replace('.','',1)#replace vai procurar o 1º'.' e trocar por ''(vazio/nada) 
    
    if notas_semponto.isdigit():#Se for apenas numericos
        notas_semponto = float(entrada_notas_str)# notas_semponto recebe o valor castado em FLOAT

        if notas_semponto <= 10:        
            lista_notas.append(notas_semponto)#Lista aprende os valores validos
        else:
            print(f'Valor inválido.')


    else:# se n for só numerico
        print('Informe apenas numeros de (0.0 a 10.00).')

for nota in lista_notas:# para cada nota na lista
    if nota >= 7:#Verifica se a nota é maior q 7 
        lista_media.append(nota)#Adiciona a uma lista

print(f'Foram informadas {len(lista_notas)} de notas.\nNOTAS |----> {lista_notas}')
media = sum(lista_notas) / len(lista_notas)
print(f'A Média da turma foi {media:.1f}')#Ajuste para 1 casa decimal
print(f'Alunos que que ficaram acima da media {len(lista_media)} alunos.')
