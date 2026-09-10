# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
#Exercício 4 - Validador de CPF
#Crie uma função validar_cpf(cpf). Ela deve verificar:
#possui exatamente 11 caracteres?
#todos são números?
#Se sim, retorne True.
#Caso contrário, retorne False.
#Não é necessário validar os dígitos verificadores.

from time import sleep

# Valida o CPF de acordo com a regra implementada no exercício.
def validar_cpf(cpf):
    from time import sleep   

    # Verificação de 11 caracteres
    print(f'Analizando quantidade de caractéres...')
    sleep(1.75)    
    if len(cpf) == 11:
        qnt_valida = True
        print(f'Quantidade [OK]. ')

    else:
        qnt_valida = False
        print('Quantidade: [ERRO]')

    # Vericação se são nmericos
    print(f'Analisando se são apenas números...')
    sleep(1.75)
    if cpf.isdigit():
        cpf_numerico = True
        print('Númerico: [OK]')
    else:
        cpf_numerico = False
        print(f'Númerico: [FALSE]')

    
        

    # é valido ?
    cpf_valido = qnt_valida and cpf_numerico
    print(f'Verificando se o CPF é valido....')
    sleep(2)
    if cpf_valido == True:
        print(f' CPF VALIDO.')
        print(f'Preenche todos os requisitos.')
    else:
        print('CPF INVALIDO')
    return cpf_valido



# Programa principal

entrada_cpf = input('CPF: ').strip().replace(' ','')

verificacao_cpf = validar_cpf(entrada_cpf)
