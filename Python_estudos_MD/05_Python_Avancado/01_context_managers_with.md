# Context Managers (with)

## Explicação informal

Você já usou isso sem saber o nome: `with open("arquivo.txt") as f:`. Esse `with` garante que o arquivo seja **fechado automaticamente** no final do bloco, mesmo se der erro no meio do caminho.

Um context manager é como um "assistente" que cuida de abrir e fechar/liberar um recurso pra você — arquivo, conexão de banco de dados, lock de concorrência — sem você precisar lembrar de fechar manualmente (e sem correr o risco de esquecer, o que causaria vazamento de recursos).

## Explicação formal

Context manager é um objeto que define um contexto de execução através dos métodos `__enter__` e `__exit__`, permitindo que recursos sejam **alocados e liberados automaticamente**, mesmo em caso de exceção, usando a instrução `with`.

### O exemplo mais comum: arquivos

```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# aqui fora do "with", o arquivo já foi fechado automaticamente
```

Isso é equivalente (mas muito mais seguro) do que fazer manualmente:

```python
arquivo = open("dados.txt", "r", encoding="utf-8")
try:
    conteudo = arquivo.read()
finally:
    arquivo.close()  # se você esquecer isso, o arquivo fica "vazando" aberto
```

### Como funciona por dentro: `__enter__` e `__exit__`

Qualquer classe pode virar um context manager implementando esses dois métodos:

```python
class MeuContexto:
    def __enter__(self):
        print("Entrando no contexto...")
        return self   # o que for retornado aqui vira o "as variavel"

    def __exit__(self, tipo_erro, valor_erro, traceback):
        print("Saindo do contexto...")
        # retornar True aqui "engoliria" uma exceção; False deixa ela propagar


with MeuContexto() as ctx:
    print("Dentro do bloco with")

# Entrando no contexto...
# Dentro do bloco with
# Saindo do contexto...
```

### `__exit__` é chamado MESMO se der erro

Essa é a grande vantagem sobre fazer manualmente:

```python
class MeuContexto:
    def __enter__(self):
        print("Abrindo recurso")
        return self

    def __exit__(self, tipo_erro, valor_erro, traceback):
        print("Fechando recurso (sempre executa, mesmo com erro!)")
        return False  # não engole a exceção, ela continua subindo

with MeuContexto():
    print("Fazendo algo...")
    raise ValueError("Deu erro aqui!")

# Abrindo recurso
# Fazendo algo...
# Fechando recurso (sempre executa, mesmo com erro!)
# ValueError: Deu erro aqui! (o erro ainda "sobe" normalmente)
```

### Criando um context manager de forma mais simples: `@contextmanager`

O módulo `contextlib` oferece um jeito mais curto de criar context managers, usando uma função geradora ao invés de uma classe inteira:

```python
from contextlib import contextmanager

@contextmanager
def meu_contexto():
    print("Entrando...")
    yield "algum valor"   # tudo antes do yield = __enter__ / tudo depois = __exit__
    print("Saindo...")

with meu_contexto() as valor:
    print(f"Dentro do bloco, valor = {valor}")

# Entrando...
# Dentro do bloco, valor = algum valor
# Saindo...
```

### Outros exemplos comuns de context managers na biblioteca padrão

```python
# Lock de concorrência (threading)
import threading
lock = threading.Lock()

with lock:
    print("Seção crítica protegida")
    # lock é liberado automaticamente ao sair do bloco

# Múltiplos context managers no mesmo with
with open("entrada.txt") as origem, open("saida.txt", "w") as destino:
    destino.write(origem.read())
```

---

## Conteúdo bônus (extra — fora do escopo básico)

- **`contextlib.suppress`**: forma curta de ignorar exceções específicas, alternativa a um `try/except: pass`.
- **`ExitStack`**: permite gerenciar um número dinâmico de context managers (ex: abrir uma quantidade variável de arquivos).
- **Async context managers** (`__aenter__` / `__aexit__`): versão para código assíncrono, usados com `async with`.

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    with open("arquivo_que_nao_existe.txt") as f:
        conteudo = f.read()
# Se o arquivo não existir, o erro é silenciado, sem precisar de try/except explícito
print("Programa continua normalmente")
```
