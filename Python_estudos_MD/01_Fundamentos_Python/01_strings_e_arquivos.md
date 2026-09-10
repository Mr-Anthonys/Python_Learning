# Manipulação de Arquivos e Strings em Python — Guia Completo

## Sumário
### Parte 1 — Strings
1. [O que é uma string](#1-o-que-é-uma-string)
2. [Indexação e slicing de strings](#2-indexação-e-slicing-de-strings)
3. [Métodos essenciais de strings](#3-métodos-essenciais-de-strings)
4. [Formatação de strings](#4-formatação-de-strings)
5. [Strings são imutáveis](#5-strings-são-imutáveis)
6. [Expressões regulares (regex)](#6-expressões-regulares-regex)

### Parte 2 — Arquivos
7. [Abrindo arquivos](#7-abrindo-arquivos)
8. [Modos de abertura](#8-modos-de-abertura)
9. [Lendo arquivos](#9-lendo-arquivos)
10. [Escrevendo em arquivos](#10-escrevendo-em-arquivos)
11. [Trabalhando com CSV](#11-trabalhando-com-csv)
12. [Trabalhando com JSON](#12-trabalhando-com-json)
13. [Manipulando caminhos com pathlib](#13-manipulando-caminhos-com-pathlib)
14. [Boas práticas](#14-boas-práticas)
15. [Erros comuns](#15-erros-comuns)

---

## 1. O que é uma string

Uma sequência de caracteres, usada para representar texto. Em Python pode ser criada com aspas simples ou duplas.

```python
nome = "Python"
frase = 'Aprendendo programação'
multilinha = """Isso é
um texto
com várias linhas"""
```

---

## 2. Indexação e slicing de strings

```python
texto = "Python"

print(texto[0])     # P
print(texto[-1])    # n
print(texto[0:3])   # Pyt
print(texto[::-1])  # nohtyP (string invertida)
```

---

## 3. Métodos essenciais de strings

```python
frase = "  Python é incrível  "

print(frase.strip())        # remove espaços das pontas: "Python é incrível"
print(frase.lower())        # minúsculas
print(frase.upper())        # MAIÚSCULAS
print(frase.replace("incrível", "poderoso"))  # substitui trecho

print("Python".startswith("Py"))  # True
print("Python".endswith("on"))    # True

partes = "a,b,c".split(",")   # ['a', 'b', 'c']
unido = "-".join(["a", "b", "c"])  # "a-b-c"

print(len("Python"))          # 6
print("thon" in "Python")     # True
print("Python".find("th"))    # 2 (índice onde começa, -1 se não achar)
print("Python".count("t"))    # 1

print("123".isdigit())    # True
print("abc".isalpha())    # True
print("abc123".isalnum()) # True
```

---

## 4. Formatação de strings

**f-strings (recomendado, Python 3.6+):**

```python
nome = "Ana"
idade = 25
print(f"{nome} tem {idade} anos")
print(f"Ano que vem terá {idade + 1} anos")  # pode fazer operações dentro

# Formatação de números
pi = 3.14159
print(f"{pi:.2f}")   # 3.14 (duas casas decimais)
preco = 1500
print(f"R$ {preco:,.2f}")  # R$ 1,500.00
```

**Outras formas (mais antigas, mas ainda vistas em código legado):**

```python
# .format()
print("{} tem {} anos".format(nome, idade))

# operador %
print("%s tem %d anos" % (nome, idade))
```

---

## 5. Strings são imutáveis

Uma vez criada, uma string não pode ser alterada diretamente — qualquer "modificação" cria uma nova string.

```python
texto = "Python"
texto[0] = "J"  # ERRO: TypeError

# Correto: criar uma nova string
novo_texto = "J" + texto[1:]
print(novo_texto)  # Jython
```

---

## 6. Expressões regulares (regex)

Usadas para busca e validação de padrões complexos em texto, através do módulo `re`.

```python
import re

texto = "Meu telefone é 11 98765-4321"

# Buscar um padrão
resultado = re.search(r"\d{2} \d{5}-\d{4}", texto)
if resultado:
    print(resultado.group())  # 11 98765-4321

# Validar formato de e-mail (exemplo simples)
email = "teste@exemplo.com"
if re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email):
    print("E-mail válido")

# Substituir padrões
texto_limpo = re.sub(r"\d+", "", "Python3 é ótimo em 2026")
print(texto_limpo)  # "Python é ótimo em "
```

---

## 7. Abrindo arquivos

```python
arquivo = open("dados.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
arquivo.close()  # sempre fechar o arquivo depois de usar
```

**Forma recomendada — usando `with` (fecha o arquivo automaticamente):**

```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
# o arquivo já é fechado automaticamente ao sair do bloco with
```

---

## 8. Modos de abertura

| Modo | Significado |
|---|---|
| `"r"` | Leitura (padrão) — erro se o arquivo não existir |
| `"w"` | Escrita — cria o arquivo ou **sobrescreve** se já existir |
| `"a"` | Acréscimo (append) — adiciona ao final sem apagar o conteúdo |
| `"x"` | Criação — erro se o arquivo já existir |
| `"r+"` | Leitura e escrita |
| `"rb"` / `"wb"` | Modo binário (imagens, PDFs, etc.) |

---

## 9. Lendo arquivos

```python
# Ler tudo de uma vez
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Ler linha por linha (economiza memória em arquivos grandes)
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove a quebra de linha \n

# Ler todas as linhas em uma lista
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()  # lista, cada item é uma linha
```

---

## 10. Escrevendo em arquivos

```python
# Sobrescrever o conteúdo
with open("saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")

# Adicionar ao final sem apagar o que já existe
with open("saida.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Nova linha adicionada\n")

# Escrever várias linhas de uma vez
linhas = ["linha 1\n", "linha 2\n", "linha 3\n"]
with open("saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(linhas)
```

---

## 11. Trabalhando com CSV

```python
import csv

# Lendo um CSV
with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)  # cada linha vira uma lista

# Lendo como dicionário (usa a primeira linha como cabeçalho)
with open("dados.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha["nome"], linha["idade"])

# Escrevendo um CSV
with open("saida.csv", "w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["nome", "idade"])
    escritor.writerow(["Ana", 25])
```

---

## 12. Trabalhando com JSON

```python
import json

# Convertendo objeto Python -> JSON (string)
dados = {"nome": "Ana", "idade": 25, "hobbies": ["ler", "programar"]}
texto_json = json.dumps(dados, indent=4, ensure_ascii=False)
print(texto_json)

# Salvando em arquivo
with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Lendo JSON de um arquivo -> objeto Python
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)
    print(dados_lidos["nome"])

# Convertendo string JSON -> objeto Python
objeto = json.loads('{"a": 1, "b": 2}')
```

---

## 13. Manipulando caminhos com pathlib

Forma moderna (recomendada) de trabalhar com caminhos de arquivos, mais legível que `os.path`.

```python
from pathlib import Path

caminho = Path("pasta/subpasta/arquivo.txt")

print(caminho.name)      # arquivo.txt
print(caminho.suffix)    # .txt
print(caminho.parent)    # pasta/subpasta
print(caminho.exists())  # True/False

# Criar pastas
Path("nova_pasta").mkdir(exist_ok=True)

# Listar arquivos de uma pasta
for arquivo in Path(".").glob("*.txt"):
    print(arquivo)
```

---

## 14. Boas práticas

- Sempre use `with open(...)` — garante que o arquivo será fechado mesmo se ocorrer erro
- Sempre especifique `encoding="utf-8"` para evitar problemas com acentuação
- Use f-strings para formatação — são mais legíveis e rápidas
- Para arquivos grandes, leia linha por linha em vez de `.read()` de uma vez
- Prefira `pathlib` a `os.path` em código novo

---

## 15. Erros comuns

1. **Esquecer de fechar o arquivo** (quando não usa `with`) — pode causar vazamento de recursos.
2. **Abrir em modo `"w"` sem querer** e sobrescrever um arquivo importante — use `"a"` se a intenção é adicionar conteúdo.
3. **Não especificar `encoding`**, causando erro com acentos/caracteres especiais.
4. **Tentar modificar uma string diretamente** — strings são imutáveis, é preciso criar uma nova.
5. **FileNotFoundError** — tentar abrir em modo `"r"` um arquivo que não existe.

---

## Resumo rápido (cheat sheet)

```python
# Strings
texto.strip(); texto.lower(); texto.upper()
texto.split(","); "-".join(lista)
f"{variavel}"

# Arquivos
with open("arquivo.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()

with open("arquivo.txt", "w", encoding="utf-8") as f:
    f.write("texto")

# JSON
import json
json.dump(dados, arquivo)
json.load(arquivo)

# CSV
import csv
csv.reader(arquivo)
csv.writer(arquivo)
```
