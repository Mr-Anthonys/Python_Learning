# ============================================================
# Estudo de funções
#
# Este arquivo faz parte do material de estudo e registra uma etapa
# do aprendizado. Os comentários foram adicionados para explicar
# responsabilidades e conceitos importantes sem alterar a lógica.
# ============================================================
# Exercício 5 - Calculadora com funções
# Crie 4 funções: somar(a, b), subtrair(a, b), multiplicar(a, b), dividir(a, b)
# Cada uma deve APENAS calcular e RETORNAR o resultado (sem print dentro delas).
#
# No programa principal:
# - peça dois números ao usuário
# - peça a operação desejada (+, -, *, /)
# - chame a função correspondente à operação escolhida
# - exiba o resultado com print (fora das funções)
#
# Dica: cuidado com divisão por zero (o divisor pode vir como 0)


# Realiza a operação matemática correspondente e retorna o resultado.
def somar(a=0,b=0):
    c = a+b
    return c

# Realiza a operação matemática correspondente e retorna o resultado.
def subtrair(a=0,b=0):
    c = a-b
    return c

# Realiza a operação matemática correspondente e retorna o resultado.
def multplicacao(a=0,b=0):
    c = a*b
    return c

# Realiza a operação matemática correspondente e retorna o resultado.
def divisao(a=0,b=0):
    c = a/b
    return c

# programa principal
n1 = float(input('Informe o 1º Nº: '))
n2 = float(input('Informe o 2º Nº: '))

op = input(f'Operação desejada --> (+, -, *, /): ')

if op == '+':
    s = somar(n1,n2)
    print(s)

if op == '-':
    sub = subtrair(n1,n2)
    print(sub)

if op == '*':
    mult = multplicacao(n1,n2)
    print(mult)

if op == '/':
    try:
        div = divisao(n1,n2)
        print(f'{div:.3f}')
    except (ZeroDivisionError):
        print(f'Impossivél dividir por 0')
    
    
    

