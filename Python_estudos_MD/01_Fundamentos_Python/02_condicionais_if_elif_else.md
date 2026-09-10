# Condições em Python — Guia Completo (Básico ao Avançado)

## Sumário
1. [O que são estruturas condicionais](#1-o-que-são-estruturas-condicionais)
2. [Condição simples (if)](#2-condição-simples-if)
3. [Condição composta (if-else)](#3-condição-composta-if-else)
4. [Condições encadeadas (if-elif-else)](#4-condições-encadeadas-if-elif-else)
5. [Operadores de comparação](#5-operadores-de-comparação)
6. [Operadores lógicos (and, or, not)](#6-operadores-lógicos-and-or-not)
7. [Condições aninhadas](#7-condições-aninhadas)
8. [Operador ternário](#8-operador-ternário)
9. [Match-case (Python 3.10+)](#9-match-case-python-310)
10. [Truthy e Falsy](#10-truthy-e-falsy)
11. [Boas práticas](#11-boas-práticas)
12. [Erros comuns](#12-erros-comuns)

---

## 1. O que são estruturas condicionais

Estruturas que permitem executar diferentes blocos de código dependendo de uma condição ser verdadeira (`True`) ou falsa (`False`).

---

## 2. Condição simples (if)

```python
idade = 20

if idade >= 18:
    print("Maior de idade")
```

O bloco indentado só executa se a condição for `True`.

---

## 3. Condição composta (if-else)

```python
idade = 15

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

Sempre um dos dois blocos será executado.

---

## 4. Condições encadeadas (if-elif-else)

Usada quando há mais de duas possibilidades.

```python
nota = 7

if nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
else:
    print("Reprovado")
```

O Python testa as condições **em ordem** e para na primeira verdadeira — as próximas `elif` nem são avaliadas.

---

## 5. Operadores de comparação

| Operador | Significado |
|---|---|
| `==` | igual a |
| `!=` | diferente de |
| `>` | maior que |
| `<` | menor que |
| `>=` | maior ou igual |
| `<=` | menor ou igual |

```python
print(5 == 5)   # True
print(5 != 3)   # True
print("a" < "b")  # True (comparação alfabética)
```

---

## 6. Operadores lógicos (and, or, not)

```python
idade = 25
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")

if idade < 18 or not tem_carteira:
    print("Não pode dirigir")
```

**Tabela verdade rápida:**
- `and` → precisa que TODAS as condições sejam `True`
- `or` → basta UMA condição ser `True`
- `not` → inverte o valor lógico

**Short-circuit evaluation**: Python para de avaliar assim que o resultado já está definido.

```python
def checar():
    print("Função chamada")
    return True

# 'checar()' nunca é executada, pois False and X já é False
print(False and checar())
```

---

## 7. Condições aninhadas

Um `if` dentro de outro `if`.

```python
usuario_logado = True
eh_admin = True

if usuario_logado:
    if eh_admin:
        print("Acesso total ao painel")
    else:
        print("Acesso limitado")
else:
    print("Faça login")
```

> Muitas condições aninhadas deixam o código difícil de ler — geralmente pode ser simplificado combinando com `and`/`or`.

```python
# Em vez de aninhar, pode combinar:
if usuario_logado and eh_admin:
    print("Acesso total ao painel")
```

---

## 8. Operador ternário

Forma resumida de escrever um `if-else` simples em uma linha.

```python
idade = 20
status = "Maior" if idade >= 18 else "Menor"
print(status)  # Maior

# Equivalente a:
if idade >= 18:
    status = "Maior"
else:
    status = "Menor"
```

Pode encadear (com moderação, senão fica ilegível):

```python
nota = 7
conceito = "A" if nota >= 9 else "B" if nota >= 7 else "C"
```

---

## 9. Match-case (Python 3.10+)

Similar ao `switch` de outras linguagens — útil para comparar um valor com vários padrões possíveis.

```python
def resposta_http(codigo):
    match codigo:
        case 200:
            return "OK"
        case 404:
            return "Não encontrado"
        case 500:
            return "Erro no servidor"
        case _:
            return "Código desconhecido"

print(resposta_http(404))  # Não encontrado
```

Suporta padrões mais complexos, como listas e classes:

```python
def analisar_comando(comando):
    match comando.split():
        case ["ligar", dispositivo]:
            print(f"Ligando {dispositivo}")
        case ["desligar", dispositivo]:
            print(f"Desligando {dispositivo}")
        case _:
            print("Comando não reconhecido")

analisar_comando("ligar luz")  # Ligando luz
```

---

## 10. Truthy e Falsy

Em Python, qualquer valor pode ser avaliado como verdadeiro ou falso dentro de um `if`, mesmo sem uma comparação explícita.

**Valores considerados "Falsy" (equivalentes a False):**
```python
0, 0.0, "", [], {}, (), set(), None, False
```

**Tudo o resto é "Truthy" (equivalente a True):**

```python
lista = []
if lista:
    print("Tem itens")
else:
    print("Lista vazia")  # isso será impresso

nome = "Ana"
if nome:
    print("Nome preenchido")  # isso será impresso
```

---

## 11. Boas práticas

- Evite condições muito aninhadas — prefira combinar com `and`/`or` ou usar "early return"
- Use nomes de variáveis booleanas claros: `esta_ativo`, `tem_permissao`
- Prefira `if valor:` a `if valor == True:` (redundante)
- Para checar `None`, use `is None` em vez de `== None`

```python
# Early return: reduz aninhamento
def verificar_acesso(usuario):
    if not usuario.esta_logado:
        return "Faça login"
    if not usuario.eh_admin:
        return "Acesso negado"
    return "Acesso liberado"
```

---

## 12. Erros comuns

1. **Confundir `=` (atribuição) com `==` (comparação)** — `if x = 5:` gera erro de sintaxe.
2. **Indentação incorreta** — Python usa indentação para definir os blocos; misturar espaços e tabs quebra o código.
3. **Comparar `None` com `==`** — o correto é `is None` / `is not None`.
4. **Excesso de `elif`** — quando há muitas opções fixas, `match-case` ou um dicionário podem ser mais legíveis.
5. **Esquecer que `and`/`or` fazem short-circuit**, o que pode mascarar bugs se uma função com efeito colateral for chamada dentro da condição.

---

## Resumo rápido (cheat sheet)

```python
# Simples
if condicao:
    ...

# Composta
if condicao:
    ...
else:
    ...

# Encadeada
if condicao1:
    ...
elif condicao2:
    ...
else:
    ...

# Ternário
resultado = "A" if condicao else "B"

# Match-case
match valor:
    case 1:
        ...
    case _:
        ...
```
