# ============================================================
# Exercício de laços de repetição
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================

#Exercício 4:
#region
# Calcúlo de média: Leia quantos alunos tem na sala.
# Depois pedir a nota final de cada aluno.
# E no final mostrar a média da SALA !

lista_notas = [] #Criando uma lista vazia []

while True:
    entrada = input('Quantidade de alunos: ').strip()#Entrada da quantidade de alunos    
    if entrada.isdigit():# Verificar se a resposta foi númerico
        alunos = int(entrada)#Alunos recebe o valor da entrada convertido em INT()

        break# Tudo OK eu encerro o laço
    else:# Não foi númerico
        print('Informação ínvalida.')#repete  laço

for p in range(1, alunos + 1):#Para cada p em alunos(entrada) +1 (o range exclui o ultimo numero) faça:
    while True:
        entrada_2 = input(f'Nota final do {p}º Aluno: ').strip().replace(',', '.')# Se usar , trocar para .
        entrada_semponto = entrada_2.replace('.','',1)#Verifica se tem '.' na entrada e troca por ''(nada) o 1 garante q remove só 1º ponto       
        if entrada_semponto.isdigit() and entrada_2.count('.')<=1:# entrada sem ponto é somente digito(removi pelo replace) e exite 1 ou menos ponto na entrada 2 faça:
            notas = float(entrada_2)# Aqui pego a entrada 2 (nota correta) converto para float            
            lista_notas.append(notas)#salvo a nota dentro da lista
            break
        else:
            print(f'Nota inválida, Informe novamente')
media = sum(lista_notas) / len(lista_notas)

print(f'A média da sala com {alunos} alunos foi de {media:.2f}')