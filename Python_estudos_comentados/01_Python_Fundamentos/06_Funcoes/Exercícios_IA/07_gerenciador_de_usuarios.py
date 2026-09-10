# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercício Gerenciador de Usuários
#Utilize uma lista. Crie as funções: adicionar_usuario(), remover_usuario(), listar_usuarios()
#Monte um menu.
#1 - Adicionar usuário
#2 - Remover usuário
#3 - Buscar usuário
#4 - Listar usúarios
#5 - Estastisticas
#6 - Sair




# Exibe uma linha/separador para organizar a interface.
def linha():
    print(f'='*30)


# Adiciona um item aos dados utilizados pelo programa.
def adicionar(lista):
    """
Cadastrar 1 nome.
Args:
    Uma lista para ter o nome cadastrado.
Return:
    Uma exibição do nome cadastrado e a lista.
OBS: 
    Possui uma função aninhada chamada, linha() onde realiza um print('='*nº)
    """
# Teste de validação com Try.
    while True:
        nome = input(f'Informe o usuário ser cadastrado: ').strip().lower()
        if ' 'in nome:
            print(f'Não pode conter espaços')
            continue
        else:
            lista.append(nome)
            linha()                    
            print(f'Usuário {nome.title()}, cadastrado com sucesso.')            
            break
    return lista
        

# Remove um item dos dados utilizados pelo programa.
def remover(lista):
    """
Recebe uma entrada STR sem espaços adjasentes de um nome a ser removido.
Args:
    Uma lista para verificar nome cadastrado a ser removido.
Return:
    Sem retorno, apenas prints de sucesso ou falha na remoção do nome.
OBS: 
    Possui uma função aninhada chamada, linha() onde realiza um print('='*nº)
    """
    
    nome = input(f'Remover o usuário: ').strip().lower()
    linha()
    if nome in lista:
        lista.remove(nome)        
        print(f'{nome.title()} Removido com sucesso.')
        linha()
        
    else:
        print(f'Usuário não encontrado.')
        

# Exibe/lista os dados armazenados para facilitar a visualização dos resultados.
def listar_usuarios(lista):

    """
Exibe o conteúdo da lista de forma formatada.
Args:
    lista a ser formatada
Return:
    Sem retorno, apenas print com os elementos da lista formatados.
OBS: 
    Possui uma função aninhada chamada, linha() onde realiza um print('='*nº)
    """
    linha()
    print(f'{"LISTA DE USUÁRIOS":^30}')
    for i, u in enumerate(lista):
        print(f'{i+1}º Usuário --> {u}')


# Procura uma informação nos dados disponíveis e trabalha com o resultado encontrado.
def buscar(lista):
    nome = input('Buscar usuário: ').strip().lower()    
    if nome in lista:
        print(f'Usuário {nome} encontrado. ')
    else:
        print(f'Usuário {nome} não cadastrado.')


# Calcula/exibe estatísticas dos dados trabalhados pelo programa.
def estastisticas(lista):
    maior = 0  
    print(f'{"ESTASTÍSTICAS":_^30}')
    linha()
    print(f'Total de usuários --> {len(lista)}')
    print(f'Primeiro usuário --> {lista[0]}')
    print(f'Último usuário --> {lista[-1]}')
    #Descobrindo a quantidade de letra e o maior NOME
    for i, nome in enumerate(lista):
        if len(nome) > maior:
            maior = len(nome)
            nome_maior = nome
            #Optei por ñ usar o return e apenas mostrar formatado
            print(f'Maior nome foi --> "{nome_maior}" com {maior} letras.')
    linha()



# Apresenta o menu e organiza as opções de interação do programa.
def menu(lista):
    """
Um menu Gerenciamento de cadastro de usuarios.

    """

    while True:
        linha()
        print(f'{"MENU":^30}')
        linha()
        print(f'1 - Adicionar usuário')
        print(f'2 - Remover usuário')
        print(f'3 - Buscar usuário')
        print(f'4 - Listar usuários')
        print(f'5 - Estastísticas')
        print(f'6 - Sair')
        linha()

        
        r_str = input(f'Informe uma opção:  ').strip().lower()# Entrada da resposta
        linha()
        if not r_str.isdigit():# verifica se não é somente numeros.
            print(f'Informe somente números !')
            continue# Volta para o inicio do laço e ignora as linhas abaixo

        
        r = int(r_str)

        if r > 0 and r < 7:

            if r == 1:
                adicionar(lista)
                
            elif r == 2:
                remover(lista)

            elif r == 3:
                buscar(lista)

            elif r == 4:
                listar_usuarios(lista) 

            elif r == 5 :
                estastisticas(lista)

            elif r == 6:
                break

        else:
            print(f'Opção "{r}" Inválida !\nEscolha novamente. ')



# programa Principal. 
gerenciamento_usuario = []
menu(gerenciamento_usuario)
print(f'Finalizando o gerenciamento de usuários...')
print(f'ATÉ LOGO.')


