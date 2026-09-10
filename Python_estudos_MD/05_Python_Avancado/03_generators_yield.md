# Generators

## Explicação informal

Imagina que você precisa processar 10 milhões de linhas de um arquivo. Se você criar uma lista com tudo isso na memória de uma vez, seu computador pode travar.

Um generator é como uma "torneira": ao invés de encher um balde inteiro (lista) de uma vez, ele entrega os valores **um de cada vez, sob demanda**, conforme você pede. Isso economiza muita memória.

## Explicação formal

Um generator é um tipo especial de iterável que **produz valores sob demanda (lazy evaluation)**, um de cada vez, em vez de calcular e armazenar todos os valores na memória de uma só vez. É criado usando uma função com a palavra-chave `yield` no lugar de `return`, ou através de uma *generator expression*.

### Função geradora — usando `yield`

```python
def contar_ate(numero):
    contador = 1
    while contador <= numero:
        yield contador   # "pausa" a função aqui e entrega o valor
        contador += 1

gerador = contar_ate(5)
print(gerador)   # <generator object contar_ate at 0x...>

for numero in gerador:
    print(numero)
# 1
# 2
# 3
# 4
# 5
```

### A diferença entre `return` e `yield`

- `return` **encerra** a função e devolve um valor final.
- `yield` **pausa** a função, entrega um valor, e na próxima chamada continua **exatamente de onde parou** (mantém o estado interno).

```python
def funcao_normal():
    return [1, 2, 3]   # calcula tudo de uma vez, guarda tudo na memória

def funcao_geradora():
    yield 1
    yield 2
    yield 3   # entrega um valor por vez, sob demanda
```

### Usando `next()` manualmente

```python
def contar_ate(numero):
    contador = 1
    while contador <= numero:
        yield contador
        contador += 1

gerador = contar_ate(3)

print(next(gerador))  # 1
print(next(gerador))  # 2
print(next(gerador))  # 3
print(next(gerador))  # StopIteration (acabaram os valores)
```

### Generator Expression (versão "compacta")

Parecido com list comprehension, mas com parênteses `()` em vez de colchetes `[]`:

```python
quadrados_lista = [x ** 2 for x in range(1000000)]   # cria TUDO na memória agora
quadrados_gerador = (x ** 2 for x in range(1000000))  # não cria nada ainda, só quando pedir

print(sum(quadrados_gerador))  # calcula sob demanda, sem guardar a lista inteira
```

### Por que usar generator em vez de lista?

| Lista | Generator |
|---|---|
| Guarda tudo na memória de uma vez | Guarda só o estado atual |
| Pode percorrer múltiplas vezes | Só percorre **uma vez** (depois "acaba") |
| `len()` funciona | `len()` **não** funciona |
| Bom para conjuntos pequenos | Bom para grandes volumes de dados ou fluxos infinitos |

```python
def numeros_pares_infinitos():
    numero = 0
    while True:              # gerador "infinito" -- só é possível por ser lazy
        yield numero
        numero += 2

pares = numeros_pares_infinitos()
for i, par in enumerate(pares):
    if i >= 5:
        break
    print(par)
# 0, 2, 4, 6, 8
```

Uma lista infinita seria impossível de criar (travaria o computador). Um generator infinito funciona porque só calcula um valor por vez.

---

## Conteúdo bônus (extra — fora do escopo básico)

- **`yield from`**: delega a geração de valores para outro generator/iterável, útil em generators aninhados.
- **Generators com estado bidirecional** (`.send()`): permite "enviar" valores de volta para dentro do generator, não só receber.
- **Combinar com `itertools`**: módulo nativo cheio de ferramentas para trabalhar com iteráveis/generators (`itertools.islice`, `itertools.chain`, etc).

```python
import itertools

def gerador_a():
    yield 1
    yield 2

def gerador_b():
    yield from gerador_a()  # delega para outro generator
    yield 3

for valor in gerador_b():
    print(valor)
# 1, 2, 3

# Pegando só os 5 primeiros valores de um generator infinito
def contar_infinito():
    n = 0
    while True:
        yield n
        n += 1

primeiros_5 = list(itertools.islice(contar_infinito(), 5))
print(primeiros_5)  # [0, 1, 2, 3, 4]
```
