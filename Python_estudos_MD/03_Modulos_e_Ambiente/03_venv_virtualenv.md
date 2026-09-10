# Virtualenv / venv

## Explicação informal

Imagina que você tem vários projetos Python no seu computador, e cada um precisa de versões diferentes de uma mesma biblioteca (um projeto precisa do Django 3, outro do Django 5). Se você instalar tudo "globalmente" no seu Python, vai dar conflito.

Um ambiente virtual (venv) é como criar uma "caixa isolada" pra cada projeto, com seu próprio Python e suas próprias bibliotecas, sem bagunçar o resto do sistema nem os outros projetos.

## Explicação formal

Um ambiente virtual é uma instalação isolada do Python (interpretador + bibliotecas) usada para um projeto específico, evitando conflitos de dependências entre projetos diferentes. `venv` é o módulo nativo do Python para criar esses ambientes (não precisa instalar nada extra).

### Por que usar ambiente virtual?

- Cada projeto pode ter versões diferentes das mesmas bibliotecas, sem conflito.
- Evita "sujar" a instalação global do Python com pacotes que só um projeto usa.
- Facilita reproduzir o ambiente em outra máquina (via `requirements.txt`).
- Prática padrão no mercado — praticamente todo projeto Python sério usa.

### Criando um ambiente virtual

```bash
# Sintaxe geral
python -m venv nome_do_ambiente

# Convenção comum: chamar de "venv" ou ".venv"
python -m venv venv
```

Isso cria uma pasta `venv/` no seu projeto, contendo uma cópia isolada do interpretador Python e um local próprio para instalar bibliotecas.

### Ativando o ambiente virtual

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

Quando ativado, o terminal mostra o nome do ambiente entre parênteses, indicando que está ativo:
```
(venv) C:\Users\usuario\meu_projeto>
```

### Instalando pacotes dentro do ambiente

Com o ambiente ativado, qualquer `pip install` instala **só dentro daquele ambiente**, não globalmente:

```bash
(venv) pip install requests
(venv) pip install pandas
```

### Desativando o ambiente

```bash
deactivate
```

### Salvando e reproduzindo dependências (`requirements.txt`)

```bash
# Gera um arquivo com todas as bibliotecas instaladas no ambiente
(venv) pip freeze > requirements.txt

# Em outra máquina/projeto, instala tudo de uma vez a partir do arquivo
(venv) pip install -r requirements.txt
```

---

## Passo a passo: criando e usando venv no VSCode

1. **Abra a pasta do projeto no VSCode** (`File > Open Folder`).

2. **Abra o terminal integrado** (`Ctrl + '` ou menu `Terminal > New Terminal`).

3. **Crie o ambiente virtual** digitando no terminal:
   ```bash
   python -m venv venv
   ```

4. **Ative o ambiente** (o comando muda conforme seu terminal — veja seção acima). O VSCode geralmente detecta automaticamente e pergunta:
   > *"We noticed a new environment has been created. Do you want to select it for the workspace folder?"*
   
   Clique em **"Yes"** — isso já conecta o VSCode ao ambiente virtual.

5. **Selecionando manualmente o interpretador** (caso o VSCode não pergunte sozinho):
   - Pressione `Ctrl + Shift + P` para abrir a paleta de comandos.
   - Digite e selecione **"Python: Select Interpreter"**.
   - Escolha o interpretador que aparece com o caminho `.\venv\Scripts\python.exe` (Windows) ou `./venv/bin/python` (Linux/macOS) — geralmente marcado como `('venv': venv)`.

6. **Confirme que está usando o ambiente correto**: no canto inferior direito da barra de status do VSCode, deve aparecer o nome do interpretador selecionado (ex: `Python 3.12.0 ('venv': venv)`).

7. **Instale as bibliotecas do projeto** pelo terminal integrado do VSCode (já com o venv ativo):
   ```bash
   pip install requests pandas
   ```

8. **(Opcional) Adicione `venv/` ao `.gitignore`** — a pasta do ambiente virtual **não deve** ser versionada no Git (é pesada e específica de cada máquina):
   ```
   venv/
   __pycache__/
   ```

> Dica: sempre que abrir o projeto de novo, o VSCode lembra o interpretador selecionado (fica salvo em `.vscode/settings.json`), mas o terminal pode precisar ser ativado manualmente de novo dependendo da configuração.

---

## Conteúdo bônus (extra — fora do escopo básico)

- **`virtualenv`** (biblioteca de terceiros): mais antiga que `venv`, um pouco mais rápida e com mais opções — hoje `venv` (nativo) é suficiente para a maioria dos casos.
- **`pyenv`**: gerencia múltiplas *versões do próprio Python* (não só ambientes) — útil quando você precisa alternar entre Python 3.9, 3.11, 3.12, etc.
- **`poetry`** e **`uv`**: ferramentas modernas que combinam gerenciamento de dependências + ambiente virtual + empacotamento em uma coisa só, cada vez mais populares no mercado.

```bash
# Exemplo: verificando qual Python está ativo dentro do ambiente virtual
(venv) python -c "import sys; print(sys.executable)"
# Mostra o caminho apontando para dentro da pasta venv/, confirmando o isolamento
```
