# Dicionários em Python — Guia Completo (Básico ao Avançado)

## Sumário
1. [O que é um dicionário](#1-o-que-é-um-dicionário)
2. [Criando dicionários](#2-criando-dicionários)
3. [Acessando valores](#3-acessando-valores)
4. [Adicionando, alterando e removendo](#4-adicionando-alterando-e-removendo)
5. [Métodos essenciais](#5-métodos-essenciais)
6. [Percorrendo dicionários](#6-percorrendo-dicionários)
7. [Dicionários aninhados](#7-dicionários-aninhados)
8. [Dict comprehension](#8-dict-comprehension)
9. [Verificando existência de chaves](#9-verificando-existência-de-chaves)
10. [get() vs colchetes: qual usar](#10-get-vs-colchetes-qual-usar)
11. [defaultdict e Counter](#11-defaultdict-e-counter)
12. [Merge de dicionários](#12-merge-de-dicionários)
13. [Boas práticas](#13-boas-práticas)
14. [Erros comuns](#14-erros-comuns)

---

## 1. O que é um dicionário

Uma coleção de pares **chave: valor**, não ordenada por índice numérico (mas mantém a ordem de inserção desde o Python 3.7+), mutável, onde cada chave é única.

---

## 2. Criando dicionários

```python
dicionario_vazio = {}

pessoa = {
    "nome": "Ana",
    "idade": 25,
    "profissao": "Engenheira"
}

# Usando a função dict()
outro = dict(nome="Bruno", idade=30)

# A partir de listas de tuplas
pares = [("a", 1), ("b", 2)]
d = dict(pares)  # {'a': 1, 'b': 2}
```

Chaves podem ser qualquer tipo **imutável** (string, número, tupla); valores podem ser qualquer tipo.

---

## 3. Acessando valores

```python
pessoa = {"nome": "Ana", "idade": 25}

print(pessoa["nome"])    # Ana
print(pessoa.get("idade"))  # 25

# Diferença importante:
print(pessoa["cidade"])       # ERRO: KeyError
print(pessoa.get("cidade"))   # None (não gera erro)
print(pessoa.get("cidade", "Não informado"))  # valor padrão se não existir
```

---

## 4. Adicionando, alterando e removendo

```python
pessoa = {"nome": "Ana", "idade": 25}

# Adicionar ou alterar (mesma sintaxe)
pessoa["cidade"] = "São Paulo"   # adiciona nova chave
pessoa["idade"] = 26             # altera valor existente

# Remover
del pessoa["cidade"]             # remove pela chave
idade_removida = pessoa.pop("idade")  # remove e retorna o valor
pessoa.clear()                   # remove tudo, dicionário fica {}
```

---

## 5. Métodos essenciais

```python
pessoa = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}

print(pessoa.keys())    # dict_keys(['nome', 'idade', 'cidade'])
print(pessoa.values())  # dict_values(['Ana', 25, 'São Paulo'])
print(pessoa.items())   # dict_items([('nome', 'Ana'), ('idade', 25), ('cidade', 'São Paulo')])

print(len(pessoa))       # 3
print("nome" in pessoa)  # True — verifica se a CHAVE existe
```

---

## 6. Percorrendo dicionários

```python
pessoa = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}

# Percorrendo chaves (padrão)
for chave in pessoa:
    print(chave)

# Percorrendo valores
for valor in pessoa.values():
    print(valor)

# Percorrendo chave e valor juntos (mais usado)
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
```

---

## 7. Dicionários aninhados

```python
alunos = {
    "aluno1": {"nome": "Ana", "notas": [8, 9, 7]},
    "aluno2": {"nome": "Bruno", "notas": [6, 7, 8]}
}

print(alunos["aluno1"]["nome"])       # Ana
print(alunos["aluno2"]["notas"][0])   # 6

# Percorrendo estrutura aninhada
for chave_aluno, dados in alunos.items():
    print(f"{dados['nome']}: média {sum(dados['notas']) / len(dados['notas']):.1f}")
```

---

## 8. Dict comprehension

```python
quadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Com condição
pares = {x: x**2 for x in range(10) if x % 2 == 0}

# Invertendo chave e valor
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: chave for chave, valor in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

---

## 9. Verificando existência de chaves

```python
pessoa = {"nome": "Ana", "idade": 25}

if "nome" in pessoa:
    print("Chave existe")

if "cidade" not in pessoa:
    print("Chave não existe")
```

---

## 10. get() vs colchetes: qual usar

| Forma | Comportamento se a chave não existir |
|---|---|
| `dicionario["chave"]` | Gera `KeyError` |
| `dicionario.get("chave")` | Retorna `None` |
| `dicionario.get("chave", padrao)` | Retorna o valor padrão definido |

Use `get()` quando não tiver certeza se a chave existe — evita ter que usar `try/except` ou checar com `in` antes.

---

## 11. defaultdict e Counter

Do módulo `collections`, úteis para casos comuns.

```python
from collections import defaultdict

# defaultdict: define um valor padrão automático para chaves novas
contagem = defaultdict(int)
palavras = ["python", "java", "python", "c", "python"]

for palavra in palavras:
    contagem[palavra] += 1   # não precisa checar se a chave já existe

print(contagem)  # defaultdict(<class 'int'>, {'python': 3, 'java': 1, 'c': 1})


from collections import Counter

# Counter: forma direta de contar ocorrências
contagem2 = Counter(palavras)
print(contagem2)                  # Counter({'python': 3, 'java': 1, 'c': 1})
print(contagem2.most_common(1))   # [('python', 3)] — item mais frequente
```

---

## 12. Merge de dicionários

```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Python 3.9+
mesclado = d1 | d2
print(mesclado)  # {'a': 1, 'b': 3, 'c': 4} — em conflito, prevalece d2

# Alternativa (funciona em versões anteriores)
mesclado2 = {**d1, **d2}

# update() modifica o dicionário original
d1.update(d2)
```

---

## 13. Boas práticas

- Use `.get()` para acessar chaves que podem não existir, evitando `KeyError`
- Prefira `for chave, valor in dicionario.items()` a acessar `dicionario[chave]` dentro do loop
- Use `defaultdict` ou `Counter` para evitar código repetitivo de contagem/agrupamento
- Nomeie dicionários no plural ou de forma descritiva quando representarem coleções (`alunos`, `estoque`)
- Use dict comprehension para transformações simples entre dicionários

---

## 14. Erros comuns

1. **Acessar uma chave inexistente com colchetes** — gera `KeyError`. Use `.get()` quando não tiver certeza.
2. **Usar tipo mutável (lista) como chave** — gera `TypeError`, pois chaves precisam ser "hashable" (imutáveis).
```python
d = {[1, 2]: "valor"}  # ERRO: unhashable type: 'list'
d = {(1, 2): "valor"}  # OK: tupla funciona como chave
```
3. **Modificar o dicionário durante a iteração** — pode gerar `RuntimeError`.
```python
# ERRADO
d = {"a": 1, "b": 2}
for chave in d:
    if chave == "a":
        del d[chave]  # RuntimeError: dictionary changed size during iteration

# CORRETO: iterar sobre uma cópia das chaves
for chave in list(d.keys()):
    if chave == "a":
        del d[chave]
```
4. **Confundir `.keys()`/`.values()` com listas** — são "views", que se atualizam dinamicamente; converta com `list()` se precisar de uma lista de fato.

---

## Resumo rápido (cheat sheet)

```python
# Criação
d = {"chave": "valor"}

# Acesso
d["chave"]
d.get("chave", padrao)

# Adicionar/alterar
d["nova_chave"] = valor

# Remover
del d["chave"]
d.pop("chave")
d.clear()

# Métodos
d.keys()
d.values()
d.items()

# Iteração
for chave, valor in d.items():
    ...

# Comprehension
{chave: valor for chave, valor in ... }

# Merge (Python 3.9+)
d3 = d1 | d2
```
