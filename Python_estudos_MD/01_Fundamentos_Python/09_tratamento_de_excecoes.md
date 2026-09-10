# Tratamento de Exceções em Python (try-except) — Guia Completo

## Sumário
1. [O que é uma exceção](#1-o-que-é-uma-exceção)
2. [Sintaxe básica: try-except](#2-sintaxe-básica-try-except)
3. [Capturando tipos específicos de erro](#3-capturando-tipos-específicos-de-erro)
4. [Múltiplos except](#4-múltiplos-except)
5. [else e finally](#5-else-e-finally)
6. [Capturando a mensagem de erro](#6-capturando-a-mensagem-de-erro)
7. [Lançando exceções manualmente (raise)](#7-lançando-exceções-manualmente-raise)
8. [Exceções personalizadas](#8-exceções-personalizadas)
9. [Hierarquia de exceções](#9-hierarquia-de-exceções)
10. [Context managers e exceções](#10-context-managers-e-exceções)
11. [Boas práticas](#11-boas-práticas)
12. [Erros comuns](#12-erros-comuns)

---

## 1. O que é uma exceção

Um erro que ocorre durante a execução do programa e interrompe o fluxo normal, a menos que seja "tratado". Exemplos: dividir por zero, acessar um índice inexistente, converter texto inválido para número.

```python
# Sem tratamento, o programa quebra:
numero = int("abc")  # ValueError: invalid literal for int()
```

---

## 2. Sintaxe básica: try-except

```python
try:
    numero = int(input("Digite um número: "))
    print(10 / numero)
except:
    print("Ocorreu um erro")
```

> Usar `except:` sem especificar o tipo captura **qualquer** erro — geralmente não é recomendado (ver seção de boas práticas).

---

## 3. Capturando tipos específicos de erro

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Isso não é um número válido")
except ZeroDivisionError:
    print("Não é possível dividir por zero")
```

**Exceções mais comuns:**

| Exceção | Quando ocorre |
|---|---|
| `ValueError` | Valor de tipo correto, mas conteúdo inválido (`int("abc")`) |
| `TypeError` | Operação com tipos incompatíveis (`"2" + 2`) |
| `ZeroDivisionError` | Divisão por zero |
| `IndexError` | Índice fora do intervalo de uma lista/tupla |
| `KeyError` | Chave inexistente em um dicionário |
| `FileNotFoundError` | Arquivo não encontrado |
| `AttributeError` | Método/atributo não existe para o objeto |
| `NameError` | Variável não definida |

---

## 4. Múltiplos except

```python
try:
    lista = [1, 2, 3]
    print(lista[10])
except (IndexError, KeyError):
    print("Erro de índice ou chave")
except Exception as erro:
    print(f"Outro erro ocorreu: {erro}")
```

---

## 5. else e finally

```python
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Valor inválido")
else:
    # executa somente se NÃO houve exceção
    print(f"Você digitou {numero}")
finally:
    # executa SEMPRE, com ou sem erro
    print("Fim da tentativa")
```

- `else` → roda só se o `try` não gerou erro
- `finally` → roda sempre, útil para liberar recursos (fechar arquivo, conexão, etc.)

---

## 6. Capturando a mensagem de erro

```python
try:
    resultado = 10 / 0
except ZeroDivisionError as erro:
    print(f"Erro capturado: {erro}")
    # Erro capturado: division by zero
```

---

## 7. Lançando exceções manualmente (raise)

Usado quando você quer forçar um erro em uma condição específica do seu programa.

```python
def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor

try:
    sacar(100, 200)
except ValueError as erro:
    print(erro)  # Saldo insuficiente
```

Re-lançar uma exceção (útil para logar e propagar o erro):

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Log: erro de divisão por zero")
    raise  # relança a mesma exceção
```

---

## 8. Exceções personalizadas

Criadas herdando de `Exception`, úteis para dar significado específico a erros do seu sistema.

```python
class SaldoInsuficienteError(Exception):
    """Exceção lançada quando o saldo é insuficiente para o saque."""
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError(f"Saldo de {saldo} é menor que {valor}")
    return saldo - valor

try:
    sacar(100, 150)
except SaldoInsuficienteError as erro:
    print(f"Operação negada: {erro}")
```

---

## 9. Hierarquia de exceções

Todas as exceções derivam de `BaseException`, mas na prática a maioria herda de `Exception`.

```
BaseException
 └── Exception
      ├── ValueError
      ├── TypeError
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      └── OSError
           └── FileNotFoundError
```

Capturar `Exception` pega quase todos os erros "normais" (evite capturar `BaseException`, pois inclui `KeyboardInterrupt` e `SystemExit`).

```python
try:
    codigo_arriscado()
except Exception as erro:
    print(f"Algo deu errado: {erro}")
```

---

## 10. Context managers e exceções

O `with` (visto em arquivos) já lida bem com exceções, garantindo que recursos sejam liberados mesmo se der erro:

```python
try:
    with open("arquivo.txt", "r") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
# o arquivo é fechado automaticamente, mesmo que ocorra erro dentro do with
```

---

## 11. Boas práticas

- Capture exceções **específicas**, evite `except:` genérico (mascara bugs inesperados)
- Use `finally` para liberar recursos (fechar arquivos, conexões de banco, etc.)
- Crie exceções personalizadas quando fizer sentido para o domínio do seu sistema
- Não use `try/except` para controlar fluxo normal do programa — é para casos excepcionais
- Sempre inclua uma mensagem clara ao lançar (`raise`) uma exceção

```python
# Evitar (genérico demais)
try:
    algo()
except:
    pass

# Preferir (específico e informativo)
try:
    algo()
except ValueError as erro:
    print(f"Valor inválido: {erro}")
```

---

## 12. Erros comuns

1. **Usar `except:` sem especificar o tipo** — captura tudo, inclusive erros que deveriam quebrar o programa (ex: `KeyboardInterrupt`).
2. **Capturar exceção e não fazer nada com ela (`pass`)** — esconde bugs, dificulta debug.
3. **Colocar código demais dentro do `try`** — dificulta saber exatamente onde o erro pode ocorrer.
4. **Confundir `else` com `finally`** — `else` só roda sem erro; `finally` roda sempre.
5. **Não usar `as erro`** quando precisa da mensagem/detalhe da exceção.

---

## Resumo rápido (cheat sheet)

```python
try:
    codigo_arriscado()
except TipoDeErro as erro:
    trata_o_erro(erro)
except (Erro1, Erro2):
    trata_varios_tipos()
else:
    so_roda_sem_erro()
finally:
    roda_sempre()

# Lançar exceção
raise ValueError("mensagem")

# Exceção personalizada
class MinhaExcecao(Exception):
    pass
```
