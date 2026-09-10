# Manipulação de arquivos JSON em Python

## Explicação informal

JSON é basicamente um jeito de escrever dados (parecido com um dicionário Python) que quase toda linguagem de programação consegue ler. É o "idioma universal" para trocar dados entre sistemas — APIs, arquivos de configuração, salvar dados de forma estruturada, etc.

A boa notícia: um JSON se parece **muito** com um dicionário/lista do Python. E o Python já vem com um módulo pronto (`json`) pra converter de um lado pro outro sem drama.

## Explicação formal

JSON (JavaScript Object Notation) é um formato de texto para representar dados estruturados, usando pares chave-valor (como um dicionário) e listas. Python trabalha com JSON através do módulo nativo `json`.

### Correspondência entre JSON e tipos Python

| JSON | Python |
|---|---|
| object `{}` | `dict` |
| array `[]` | `list` |
| string `"texto"` | `str` |
| number | `int` ou `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

### Lendo um arquivo JSON (`json.load`)

```python
import json

with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)  # converte JSON -> dict/list Python

print(dados)
print(type(dados))  # <class 'dict'>
```

Exemplo de `dados.json`:
```json
{
    "nome": "Ana",
    "idade": 28,
    "ativo": true,
    "cursos": ["Python", "SQL"]
}
```

### Escrevendo um arquivo JSON (`json.dump`)

```python
import json

pessoa = {
    "nome": "Carlos",
    "idade": 35,
    "ativo": True,
    "cursos": ["Git", "Linux"]
}

with open("saida.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo)  # converte dict Python -> JSON e grava no arquivo
```

### Deixando o JSON legível (indentação)

Por padrão, `json.dump` escreve tudo em uma linha só. Para formatar de forma legível:

```python
with open("saida.json", "w", encoding="utf-8") as arquivo:
    json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)
```

- `indent=4` → formata com 4 espaços de recuo, deixando legível.
- `ensure_ascii=False` → permite salvar acentos (ã, ç, é) corretamente, em vez de converter para `\uXXXX`.

### Convertendo entre string JSON e objeto Python (sem arquivo)

Às vezes você recebe um JSON como texto (ex: resposta de uma API) e não como arquivo:

```python
import json

texto_json = '{"nome": "Ana", "idade": 28}'

# JSON (string) -> dict Python
dados = json.loads(texto_json)
print(dados["nome"])  # Ana

# dict Python -> JSON (string)
dict_python = {"produto": "Caneta", "preco": 2.5}
texto = json.dumps(dict_python, indent=2)
print(texto)
```

**Resumo dos 4 métodos principais:**

| Método | Direção | Usa arquivo? |
|---|---|---|
| `json.load(arquivo)` | JSON → Python | Sim |
| `json.dump(dados, arquivo)` | Python → JSON | Sim |
| `json.loads(texto)` | JSON (string) → Python | Não |
| `json.dumps(dados)` | Python → JSON (string) | Não |

> Dica pra lembrar: métodos com **"s"** (`loads`, `dumps`) trabalham com **s**tring; sem "s" (`load`, `dump`) trabalham direto com arquivo.

---

## Conteúdo bônus (extra — fora do escopo básico)

- **Tratamento de erro ao ler JSON malformado**: `json.JSONDecodeError` é lançado quando o conteúdo não é um JSON válido.
- **`default=` em `json.dumps`**: permite serializar tipos que o JSON não entende nativamente (como `datetime`), definindo uma função de conversão.
- **`sort_keys=True`**: ordena as chaves alfabeticamente ao salvar, útil para arquivos versionados no Git (evita diffs desnecessários).

```python
import json
from datetime import datetime

def converter_data(obj):
    # função chamada quando json.dumps encontra um tipo que não sabe converter
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d")
    raise TypeError(f"Tipo não serializável: {type(obj)}")

dados = {"evento": "Reunião", "data": datetime.now()}

texto = json.dumps(dados, default=converter_data, indent=2, ensure_ascii=False)
print(texto)

# Tratando erro de JSON inválido
try:
    json.loads('{"nome": "Ana", }')  # vírgula sobrando -> JSON inválido
except json.JSONDecodeError as erro:
    print(f"JSON inválido: {erro}")
```
