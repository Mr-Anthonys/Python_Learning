# Decorators (visão geral)

## Explicação informal

Já vimos `@property`, `@abstractmethod`, `@staticmethod`. Todos esses `@algumacoisa` em cima de uma função ou método são **decorators**.

Um decorator é como uma "embalagem" que você coloca em volta de uma função para adicionar um comportamento extra, sem precisar alterar o código de dentro da função. Tipo colocar uma capa em um livro: o conteúdo continua o mesmo, mas você adicionou algo por fora.

## Explicação formal

Um decorator é uma função que **recebe outra função como argumento, adiciona algum comportamento, e retorna uma nova função** — sem modificar o código original da função decorada. É possível porque em Python, funções são "cidadãs de primeira classe" (podem ser passadas como argumento, retornadas, atribuídas a variáveis).

### A ideia por trás (antes da sintaxe `@`)

```python
def meu_decorator(funcao):
    def wrapper():
        print("Antes de executar a função")
        funcao()
        print("Depois de executar a função")
    return wrapper

def dizer_ola():
    print("Olá!")

dizer_ola = meu_decorator(dizer_ola)  # "decorando" manualmente
dizer_ola()
# Antes de executar a função
# Olá!
# Depois de executar a função
```

### Com a sintaxe `@` (o jeito de verdade)

O `@meu_decorator` acima da função é só um "atalho" para `dizer_ola = meu_decorator(dizer_ola)`:

```python
def meu_decorator(funcao):
    def wrapper():
        print("Antes de executar a função")
        funcao()
        print("Depois de executar a função")
    return wrapper

@meu_decorator
def dizer_ola():
    print("Olá!")

dizer_ola()
# Antes de executar a função
# Olá!
# Depois de executar a função
```

### Decorator para função com parâmetros

Se a função decorada recebe argumentos, o `wrapper` precisa aceitar e repassar esses argumentos (usando `*args` e `**kwargs`):

```python
def meu_decorator(funcao):
    def wrapper(*args, **kwargs):
        print("Antes...")
        resultado = funcao(*args, **kwargs)
        print("Depois...")
        return resultado
    return wrapper

@meu_decorator
def somar(a, b):
    return a + b

print(somar(2, 3))
# Antes...
# Depois...
# 5
```

### Decorators nativos que você já conhece

- `@staticmethod` — marca um método que não usa `self` nem `cls`.
- `@classmethod` — marca um método que recebe a classe (`cls`) em vez da instância.
- `@property` — transforma um método em atributo (visto no arquivo de Encapsulamento).
- `@abstractmethod` — obriga subclasses a implementar o método (visto no arquivo de Abstração).

```python
class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b  # não usa self, é praticamente uma função solta dentro da classe

print(Calculadora.somar(2, 3))  # 5 (não precisa instanciar a classe)
```

---

## Conteúdo bônus (extra — fora do escopo básico, aprofundamento leve)

- **Decorators com parâmetros próprios** (ex: `@repetir(3)`) — exigem uma "fábrica de decorators" (uma função que retorna um decorator).
- **`functools.wraps`**: preserva o nome e a documentação original da função decorada (sem isso, `funcao.__name__` fica sendo `"wrapper"`).
- **Múltiplos decorators empilhados**: você pode aplicar mais de um decorator na mesma função — eles são executados de baixo para cima.

```python
from functools import wraps

def repetir(vezes):
    # "fábrica" de decorator: uma função que retorna um decorator configurado
    def decorator(funcao):
        @wraps(funcao)  # preserva nome/docstring original da função
        def wrapper(*args, **kwargs):
            for _ in range(vezes):
                funcao(*args, **kwargs)
        return wrapper
    return decorator

@repetir(3)
def dizer_oi():
    print("Oi!")

dizer_oi()
# Oi!
# Oi!
# Oi!
```
