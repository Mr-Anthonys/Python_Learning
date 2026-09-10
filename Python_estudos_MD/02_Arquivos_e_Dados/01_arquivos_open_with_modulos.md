# Manipulação de Arquivos em Python

---

## 1. Explicação Informal

Imagina que um arquivo no computador é tipo um caderno. Pra escrever nele, ler o que já tá escrito, ou apagar alguma coisa, você primeiro precisa **abrir o caderno**. Depois de usar, você **fecha o caderno** (senão o que você escreveu pode nem ser salvo direito).

Em Python é basicamente isso: você "abre" o arquivo com a função `open()`, faz o que precisa (ler, escrever, adicionar linha), e depois "fecha" com `close()` — ou, melhor ainda, usa o `with`, que fecha o arquivo sozinho pra você, sem você precisar lembrar.

---

## 2. Explicação Formal

Em Python, a manipulação de arquivos é feita através da função embutida `open()`, que retorna um **objeto arquivo**. Esse objeto possui métodos para leitura, escrita e navegação dentro do conteúdo do arquivo.

### 2.1 Abrindo um arquivo

```python
arquivo = open("dados.txt", "r")  # r = read (leitura)
```

A função `open()` recebe dois argumentos principais:

- **Caminho do arquivo** (nome ou caminho completo)
- **Modo de abertura** (string que define o que você pode fazer com o arquivo)

### 2.2 Modos de abertura

| Modo | Significado | Observação |
|------|-------------|------------|
| `"r"` | Leitura (read) | Padrão. Erro se o arquivo não existir |
| `"w"` | Escrita (write) | Cria o arquivo se não existir; **apaga o conteúdo** se já existir |
| `"a"` | Acrescentar (append) | Adiciona ao final do arquivo, sem apagar o que já tem |
| `"x"` | Criação exclusiva | Cria o arquivo; erro se já existir |
| `"r+"` | Leitura e escrita | O arquivo precisa existir |
| `"w+"` | Escrita e leitura | Apaga o conteúdo existente |
| `"a+"` | Acrescentar e leitura | Não apaga o conteúdo |
| `"b"` | Modo binário | Combinado com outros, ex: `"rb"`, `"wb"` (imagens, PDFs, etc.) |
| `"t"` | Modo texto | Padrão, geralmente nem precisa escrever |

### 2.3 Fechando o arquivo

Sempre que você abre um arquivo com `open()`, precisa fechar com:

```python
arquivo.close()
```

Se você esquecer de fechar, o arquivo pode ficar "travado" pra outros programas, ou o conteúdo escrito pode não ser salvo de fato (fica só no buffer/memória).

### 2.4 A forma correta: usando `with`

Na prática, quase ninguém usa `open()` + `close()` manualmente. O jeito recomendado é o **context manager** `with`, que fecha o arquivo automaticamente, mesmo que aconteça um erro no meio do processo:

```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# Aqui fora do "with", o arquivo já foi fechado automaticamente
```

---

## 3. Métodos de Leitura

```python
with open("dados.txt", "r") as arquivo:
    texto_completo = arquivo.read()        # lê o arquivo inteiro como uma única string
```

```python
with open("dados.txt", "r") as arquivo:
    primeira_linha = arquivo.readline()    # lê apenas uma linha por vez
```

```python
with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()           # retorna uma lista, cada item é uma linha
```

### 3.1 Iterando linha por linha (forma mais usada hoje em dia)

```python
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())  # strip() remove o \n do final da linha
```

Essa forma é a mais eficiente para arquivos grandes, porque não carrega tudo na memória de uma vez — lê linha a linha.

---

## 4. Métodos de Escrita

```python
with open("saida.txt", "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")
```

```python
with open("saida.txt", "w") as arquivo:
    linhas = ["Linha 1\n", "Linha 2\n", "Linha 3\n"]
    arquivo.writelines(linhas)  # escreve uma lista de strings de uma vez
```

⚠️ **Atenção:** `write()` e `writelines()` **não adicionam `\n` automaticamente**. Se você não colocar, tudo vira uma linha só.

### 4.1 Acrescentando sem apagar (`"a"`)

```python
with open("saida.txt", "a") as arquivo:
    arquivo.write("Nova linha adicionada ao final\n")
```

---

## 5. Verificando se o Arquivo Existe

Antes de tentar abrir um arquivo (principalmente em modo leitura), é comum verificar se ele existe, usando o módulo `os` ou `pathlib`:

```python
import os

if os.path.exists("dados.txt"):
    print("Arquivo existe!")
else:
    print("Arquivo não encontrado.")
```

Forma mais moderna, com `pathlib`:

```python
from pathlib import Path

caminho = Path("dados.txt")

if caminho.exists():
    print("Arquivo existe!")
```

---

## 6. Trabalhando com Caminhos (Paths)

```python
from pathlib import Path

caminho = Path("pasta") / "subpasta" / "arquivo.txt"
print(caminho)  # monta o caminho corretamente pro sistema operacional (Windows/Linux/Mac)
```

O `pathlib` é a forma mais moderna e recomendada hoje em dia para trabalhar com caminhos, substituindo boa parte do uso de `os.path`.

---

## 7. Posição do "Cursor" no Arquivo (seek e tell)

```python
with open("dados.txt", "r") as arquivo:
    print(arquivo.tell())      # mostra a posição atual do cursor (em bytes)
    arquivo.seek(0)            # move o cursor para o início do arquivo
```

Isso é útil quando você lê parte do arquivo e depois precisa voltar ao começo, por exemplo.

---

## 8. Resumo dos Métodos Mais Usados no Dia a Dia

| Método | O que faz |
|--------|-----------|
| `open()` | Abre o arquivo |
| `close()` | Fecha o arquivo (evite usar manualmente, prefira `with`) |
| `read()` | Lê o arquivo inteiro |
| `readline()` | Lê uma linha |
| `readlines()` | Lê todas as linhas como lista |
| `write()` | Escreve uma string no arquivo |
| `writelines()` | Escreve uma lista de strings |
| `for linha in arquivo` | Itera linha por linha (mais usado) |
| `.strip()` | Remove espaços/quebras de linha extras |
| `os.path.exists()` / `Path.exists()` | Verifica se o arquivo existe |

---

## 🎁 Conteúdo Bônus (fora do escopo básico, pra se aprofundar depois)

Essa seção é extra — não é o "básico obrigatório", mas são coisas muito usadas no mercado e que valem a pena conhecer quando você já estiver confortável com o conteúdo acima.

### Bônus 1 — Tratando erros ao abrir arquivos (try/except)

```python
try:
    with open("nao_existe.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    # Se o arquivo não existir, cai aqui em vez de quebrar o programa
    print("Arquivo não encontrado!")
```

### Bônus 2 — Definindo o encoding (evita problemas com acentos)

```python
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    # encoding="utf-8" evita erro com acentuação (ç, ã, é...) em textos em português
    conteudo = arquivo.read()
```

### Bônus 3 — Lendo arquivos grandes sem travar a memória

```python
with open("arquivo_grande.txt", "r") as arquivo:
    for linha in arquivo:
        # processa uma linha por vez, sem carregar o arquivo inteiro na RAM
        if "erro" in linha.lower():
            print(linha)
```

### Bônus 4 — Criando pastas automaticamente antes de salvar um arquivo

```python
from pathlib import Path

pasta = Path("relatorios")
pasta.mkdir(exist_ok=True)  # cria a pasta se não existir, sem dar erro se já existir

with open(pasta / "relatorio.txt", "w") as arquivo:
    arquivo.write("Relatório gerado com sucesso!")
```

### Bônus 5 — Copiando, movendo e apagando arquivos (módulo `shutil` e `os`)

```python
import shutil
import os

shutil.copy("origem.txt", "destino.txt")   # copia o arquivo
shutil.move("destino.txt", "pasta/")       # move o arquivo pra outra pasta
os.remove("origem.txt")                    # apaga o arquivo
```

> Nota: manipulação de arquivos **JSON** e **CSV** (muito usados no dia a dia) têm suas próprias bibliotecas (`json` e `csv`) e merecem um arquivo próprio — se quiser, posso gerar depois.
