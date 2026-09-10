# Type Hints

## Explicação informal

Python não te obriga a dizer o tipo de uma variável (diferente de linguagens como Java ou C#). Mas isso às vezes dificulta entender "o que essa função espera receber" só de olhar o código.

Type hints são como "dicas" que você escreve no código dizendo "essa variável deveria ser um `int`", "essa função retorna uma `str`". Python **não obriga** nada com isso (ele não trava se você desrespeitar) — mas seu editor (VSCode) e ferramentas de checagem usam essas dicas pra te avisar de erros antes mesmo de rodar o código.

## Explicação formal

Type hints (introduzidos na PEP 484) são anotações de tipo opcionais que indicam o tipo esperado de variáveis, parâmetros e retornos de funções. Python continua sendo uma linguagem de **tipagem dinâmica** — as hints não são verificadas em tempo de execução por padrão, servem para documentação, autocompletar do editor e checagem estática (com ferramentas como `mypy`).

### Sintaxe básica em variáveis

```python
nome: str = "Ana"
idade: int = 28
altura: float = 1.65
ativo: bool = True
```

### Sintaxe em funções

```python
def somar(a: int, b: int) -> int:
    return a + b

def saudacao(nome: str) -> str:
    return f"Olá, {nome}!"

def imprimir_log(mensagem: str) -> None:  # -> None indica que não retorna nada
    print(mensagem)
```

- Os tipos antes de `->` são dos **parâmetros**.
- O tipo depois de `->` é do **retorno** da função.

### Hints com listas, dicionários e tuplas

```python
from typing import List, Dict, Tuple

nomes: List[str] = ["Ana", "Carlos", "Beatriz"]
idades: Dict[str, int] = {"Ana": 28, "Carlos": 35}
coordenada: Tuple[float, float] = (10.5, 20.3)
```

> A partir do Python 3.9+, não é mais obrigatório importar de `typing` para os tipos básicos — pode usar direto os tipos nativos em minúsculo:

```python
nomes: list[str] = ["Ana", "Carlos"]
idades: dict[str, int] = {"Ana": 28}
coordenada: tuple[float, float] = (10.5, 20.3)
```

### `Optional` — quando um valor pode ser `None`

```python
from typing import Optional

def buscar_usuario(id: int) -> Optional[str]:
    # pode retornar uma str (nome do usuário) ou None (se não encontrar)
    if id == 1:
        return "Ana"
    return None
```

`Optional[str]` é equivalente a `str | None` (sintaxe mais moderna, Python 3.10+):

```python
def buscar_usuario(id: int) -> str | None:
    ...
```

### `Union` — quando um valor pode ser de mais de um tipo

```python
from typing import Union

def processar(valor: Union[int, float]) -> float:
    return valor * 1.1

# Sintaxe moderna (Python 3.10+)
def processar(valor: int | float) -> float:
    return valor * 1.1
```

### O Python não impede você de "quebrar" o type hint

```python
def somar(a: int, b: int) -> int:
    return a + b

resultado = somar("2", "3")  # Python NÃO trava — funciona (concatena strings: "23")
```

Isso é importante entender: type hints são **documentação e ajuda para ferramentas**, não uma validação em tempo real como em outras linguagens.

---

## Conteúdo bônus (extra — fora do escopo básico)

- **`mypy`**: ferramenta de checagem estática de tipos — roda `mypy meu_arquivo.py` e ele avisa (sem executar o código) se você está usando tipos errados.
- **`TypeVar` e Generics**: para criar funções/classes genéricas que funcionam com múltiplos tipos, mas mantendo consistência.
- **`Literal`**: restringe um valor a opções específicas (ex: só aceitar `"pequeno"`, `"medio"`, `"grande"`).

```python
from typing import TypeVar, Literal

T = TypeVar("T")

def primeiro_item(lista: list[T]) -> T:
    # funciona com list[int], list[str], etc, mantendo o tipo original
    return lista[0]

Tamanho = Literal["pequeno", "medio", "grande"]

def definir_tamanho(tamanho: Tamanho) -> None:
    print(f"Tamanho escolhido: {tamanho}")

definir_tamanho("pequeno")  # OK
# definir_tamanho("gigante")  # mypy acusaria erro aqui
```
