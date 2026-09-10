# Funções em Python — Guia Completo (Básico ao Avançado)

## Sumário
1. [O que é uma função](#1-o-que-é-uma-função)
2. [Sintaxe básica](#2-sintaxe-básica)
3. [Parâmetros e argumentos](#3-parâmetros-e-argumentos)
4. [Return vs Print](#4-return-vs-print)
5. [Escopo de variáveis](#5-escopo-de-variáveis)
6. [Valores padrão (default)](#6-valores-padrão-default)
7. [*args e **kwargs](#7-args-e-kwargs)
8. [Funções como objetos de primeira classe](#8-funções-como-objetos-de-primeira-classe)
9. [Funções lambda](#9-funções-lambda)
10. [Funções aninhadas e closures](#10-funções-aninhadas-e-closures)
11. [Decoradores](#11-decoradores)
12. [Recursão](#12-recursão)
13. [Generators (yield)](#13-generators-yield)
14. [Type hints em funções](#14-type-hints-em-funções)
15. [Boas práticas](#15-boas-práticas)
16. [Erros comuns](#16-erros-comuns)

---

## 1. O que é uma função

Uma função é um bloco de código reutilizável, empacotado com um nome, que executa uma tarefa específica. Serve para:

- Evitar repetição de código (princípio **DRY** — Don't Repeat Yourself)
- Organizar e dividir problemas grandes em partes menores
- Facilitar testes e manutenção

---

## 2. Sintaxe básica

```python
def nome_da_funcao(parametro1, parametro2):
    """Docstring: explica o que a função faz (opcional, mas recomendado)."""
    resultado = parametro1 + parametro2
    return resultado

# Chamando a função
valor = nome_da_funcao(3, 5)
print(valor)  # 8
```

**Elementos:**
- `def` → palavra-chave que inicia a definição
- `nome_da_funcao` → nome escolhido (siga o padrão `snake_case`)
- `(parametro1, parametro2)` → parâmetros (entradas)
- `"""docstring"""` → documentação da função
- `return` → valor de saída (opcional)

---

## 3. Parâmetros e argumentos

- **Parâmetro**: nome definido na função (`nome`)
- **Argumento**: valor real passado na chamada (`"Maria"`)

```python
def apresentar(nome, idade):
    print(f"{nome} tem {idade} anos.")

# Argumentos posicionais (ordem importa)
apresentar("Maria", 30)

# Argumentos nomeados (ordem não importa)
apresentar(idade=30, nome="Maria")
```

---

## 4. Return vs Print

Confusão muito comum no início:

| `print()` | `return` |
|---|---|
| Apenas exibe algo na tela | Devolve um valor para ser usado depois |
| Não pode ser reaproveitado | Pode ser guardado em variável, usado em cálculos, etc. |

```python
def soma_v1(a, b):
    print(a + b)   # só mostra, não devolve nada utilizável

def soma_v2(a, b):
    return a + b   # devolve o valor

resultado = soma_v2(2, 3)
print(resultado * 10)  # 50 — funciona

resultado_errado = soma_v1(2, 3)  # imprime "5"
print(resultado_errado)  # None — não tem valor pra usar
```

Uma função sem `return` explícito sempre devolve `None`.

---

## 5. Escopo de variáveis

Variáveis criadas dentro de uma função são **locais** — só existem ali dentro.

```python
def minha_funcao():
    x = 10  # variável local
    print(x)

minha_funcao()
print(x)  # ERRO: NameError, x não existe fora da função
```

**Escopo global** vs **local**:

```python
contador = 0  # variável global

def incrementar():
    global contador  # avisa que quer usar/alterar a variável global
    contador += 1

incrementar()
print(contador)  # 1
```

> Usar `global` é geralmente considerado má prática — prefira passar valores como parâmetro e retornar o resultado.

---

## 6. Valores padrão (default)

Permitem chamar a função sem passar todos os argumentos.

```python
def saudacao(nome, mensagem="Bem-vindo(a)"):
    return f"{mensagem}, {nome}!"

print(saudacao("Ana"))                  # Bem-vindo(a), Ana!
print(saudacao("Ana", "Boa tarde"))     # Boa tarde, Ana!
```

⚠️ **Cuidado**: nunca use listas/dicionários como valor padrão diretamente — é um erro clássico:

```python
# ERRADO
def adicionar_item(item, lista=[]):
    lista.append(item)
    return lista

print(adicionar_item("a"))  # ['a']
print(adicionar_item("b"))  # ['a', 'b']  <- inesperado! a lista "lembra" do estado anterior

# CORRETO
def adicionar_item(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista
```

---

## 7. *args e **kwargs

Usados quando não se sabe de antemão quantos argumentos serão passados.

```python
def somar_tudo(*args):
    """args vira uma tupla com todos os argumentos posicionais."""
    return sum(args)

print(somar_tudo(1, 2, 3, 4))  # 10


def exibir_dados(**kwargs):
    """kwargs vira um dicionário com os argumentos nomeados."""
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_dados(nome="Ana", idade=25, cidade="São Paulo")
```

Pode combinar tudo:

```python
def funcao_completa(a, b, *args, c=10, **kwargs):
    print(a, b, args, c, kwargs)

funcao_completa(1, 2, 3, 4, c=99, extra="teste")
# 1 2 (3, 4) 99 {'extra': 'teste'}
```

---

## 8. Funções como objetos de primeira classe

Em Python, funções são "cidadãs de primeira classe" — podem ser atribuídas a variáveis, passadas como argumento e retornadas por outras funções.

```python
def cumprimentar():
    return "Olá!"

minha_variavel = cumprimentar  # sem parênteses: referência à função
print(minha_variavel())        # "Olá!"


def aplicar_funcao(func, valor):
    return func(valor)

print(aplicar_funcao(str.upper, "python"))  # "PYTHON"
```

---

## 9. Funções lambda

Funções anônimas, de uma linha, usadas para operações curtas e simples.

```python
soma = lambda a, b: a + b
print(soma(2, 3))  # 5

# Muito usada com funções como sorted(), map(), filter()
numeros = [5, 3, 8, 1]
print(sorted(numeros, key=lambda x: -x))  # [8, 5, 3, 1]

quadrados = list(map(lambda x: x**2, numeros))
print(quadrados)  # [25, 9, 64, 1]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [8]
```

> Use lambda só para lógica simples. Para algo mais complexo, uma função `def` normal é mais legível.

---

## 10. Funções aninhadas e closures

Uma função pode ser definida dentro de outra, e "lembrar" das variáveis do escopo em que foi criada (closure).

```python
def criar_multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

dobro = criar_multiplicador(2)
triplo = criar_multiplicador(3)

print(dobro(5))   # 10
print(triplo(5))  # 15
```

Aqui, `multiplicar` "guarda" o valor de `fator` mesmo depois que `criar_multiplicador` já terminou de executar — isso é uma **closure**.

---

## 11. Decoradores

Um decorador é uma função que "envolve" outra função, adicionando comportamento sem modificar seu código original. Muito usado em frameworks (Flask, Django) e para logging, autenticação, medição de tempo, etc.

```python
def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes de executar a função")
        resultado = func(*args, **kwargs)
        print("Depois de executar a função")
        return resultado
    return wrapper

@meu_decorador
def dizer_oi(nome):
    print(f"Oi, {nome}!")

dizer_oi("Carlos")
# Antes de executar a função
# Oi, Carlos!
# Depois de executar a função
```

Exemplo prático — medir tempo de execução:

```python
import time

def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio:.4f}s")
        return resultado
    return wrapper

@medir_tempo
def tarefa_demorada():
    time.sleep(1)

tarefa_demorada()
```

---

## 12. Recursão

Uma função que chama a si mesma. Precisa sempre ter uma **condição de parada** (caso base), senão gera erro de recursão infinita.

```python
def fatorial(n):
    if n == 0 or n == 1:   # caso base
        return 1
    return n * fatorial(n - 1)  # chamada recursiva

print(fatorial(5))  # 120
```

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

> Recursão é elegante, mas pode ser menos eficiente que loops para certos problemas (cada chamada consome memória na pilha).

---

## 13. Generators (yield)

Funções especiais que retornam valores "sob demanda", um de cada vez, ao invés de gerar tudo de uma vez na memória. Muito úteis para lidar com grandes volumes de dados.

```python
def contador(limite):
    numero = 0
    while numero < limite:
        yield numero
        numero += 1

for n in contador(5):
    print(n)  # 0 1 2 3 4
```

Diferença de uma função normal:
- `return` encerra a função e devolve um valor único
- `yield` "pausa" a função e devolve um valor por vez, retomando de onde parou na próxima chamada

```python
# Comparação de uso de memória
def lista_quadrados(n):
    return [x**2 for x in range(n)]  # cria tudo na memória

def gerador_quadrados(n):
    for x in range(n):
        yield x**2  # gera um valor por vez

# Para n muito grande, o generator é muito mais eficiente em memória
```

---

## 14. Type hints em funções

Ajudam a documentar e podem ser checados por ferramentas externas (não são obrigatórios em tempo de execução).

```python
def somar(a: int, b: int) -> int:
    return a + b

def saudacao(nome: str, idade: int = 18) -> str:
    return f"{nome} tem {idade} anos"

from typing import List, Dict, Optional

def processar_lista(numeros: List[int]) -> float:
    return sum(numeros) / len(numeros)

def buscar_usuario(id: int) -> Optional[str]:
    """Pode retornar str ou None."""
    usuarios = {1: "Ana", 2: "Bruno"}
    return usuarios.get(id)
```

---

## 15. Boas práticas

- Use nomes descritivos: `calcular_media()` em vez de `func1()`
- Uma função deve fazer **uma coisa só** (princípio da responsabilidade única)
- Escreva docstrings explicando o propósito, parâmetros e retorno
- Evite efeitos colaterais desnecessários (alterar variáveis globais, por exemplo)
- Prefira retornar valores a usar `print()` dentro da lógica de negócio
- Funções pequenas (idealmente até ~20 linhas) são mais fáceis de testar e entender

```python
def calcular_media(notas: List[float]) -> float:
    """
    Calcula a média de uma lista de notas.

    Args:
        notas: lista de números representando notas.

    Returns:
        A média aritmética das notas.
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)
```

---

## 16. Erros comuns

1. **Esquecer o `return`** — a função executa mas não devolve nada útil (retorna `None`).
2. **Usar mutáveis como valor padrão** (`def f(lista=[])`) — comportamento inesperado entre chamadas.
3. **Confundir parâmetro com argumento** posicional/nomeado, gerando `TypeError`.
4. **Recursão sem caso base** — gera `RecursionError`.
5. **Alterar variável global sem `global`** dentro da função — gera `UnboundLocalError`.
6. **Abusar de `*args`/`**kwargs`** deixando a função difícil de entender — use com moderação.

---

## Resumo rápido (cheat sheet)

```python
def nome(a, b=10, *args, **kwargs) -> tipo_retorno:
    """Docstring."""
    # corpo da função
    return valor

# Lambda
f = lambda x: x * 2

# Decorador
@decorador
def funcao():
    pass

# Generator
def gerador():
    yield valor

# Recursão
def recursiva(n):
    if caso_base:
        return valor
    return recursiva(n - 1)
```
