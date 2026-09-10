# CMD (Prompt de Comando do Windows) — Guia do Básico ao Avançado

## 1. O que é o CMD

O **CMD** (Command Prompt / `cmd.exe`) é o interpretador de linha de comando padrão do Windows. Permite executar programas, navegar entre pastas, manipular arquivos e automatizar tarefas por meio de comandos digitados em vez de cliques.

Para abrir:
- Atalho `Win + R`, digite `cmd` e pressione Enter
- Ou pesquise "Prompt de Comando" no menu Iniciar
- Para abrir como Administrador: clique com botão direito → "Executar como administrador"

---

## 2. Atalhos úteis do teclado

| Atalho | Função |
|---|---|
| `Tab` | Autocompletar nome de arquivo/pasta |
| `↑` / `↓` | Navegar pelo histórico de comandos digitados |
| `Ctrl + C` | Cancelar/interromper o comando em execução |
| `Esc` | Limpar a linha de comando atual |
| `F7` | Mostrar histórico de comandos em uma lista |
| `Ctrl + Home` / `Ctrl + End` | Mover cursor para início/fim do buffer de texto |
| `Ctrl + A` | Selecionar todo o texto da tela atual |
| `Alt + Enter` | Alternar entre modo janela e tela cheia |
| `Ctrl + M` | Ativar modo de seleção com o mouse (em versões mais novas) |
| `Clique direito` (na barra de título ou padrão configurado) | Colar texto copiado |

---

## 3. Comandos básicos de navegação

| Comando | Função | Exemplo |
|---|---|---|
| `cd` | Mostra ou muda o diretório atual | `cd Documentos` |
| `cd..` | Sobe um nível de pasta | `cd..` |
| `cd\` | Vai direto para a raiz do drive atual | `cd\` |
| `dir` | Lista arquivos e pastas do diretório atual | `dir` |
| `dir /a` | Lista incluindo arquivos ocultos | `dir /a` |
| `dir /s` | Lista arquivos incluindo subpastas | `dir /s` |
| `cls` | Limpa a tela | `cls` |
| `exit` | Fecha o CMD | `exit` |
| `[Letra]:` | Troca de drive (ex.: ir para o drive D:) | `D:` |

---

## 4. Manipulação de arquivos e pastas

| Comando | Função | Exemplo |
|---|---|---|
| `mkdir` ou `md` | Cria uma pasta | `mkdir Projetos` |
| `rmdir` ou `rd` | Remove uma pasta vazia | `rmdir Projetos` |
| `rmdir /s /q` | Remove uma pasta e todo o conteúdo, sem confirmação | `rmdir /s /q Projetos` |
| `del` ou `erase` | Apaga um ou mais arquivos | `del arquivo.txt` |
| `copy` | Copia arquivos | `copy origem.txt destino.txt` |
| `xcopy` | Copia arquivos e pastas (com subpastas) | `xcopy C:\Origem D:\Destino /E /H` |
| `robocopy` | Cópia robusta, ideal para backups e grandes volumes | `robocopy C:\Origem D:\Destino /E` |
| `move` | Move ou renomeia arquivos/pastas | `move arquivo.txt D:\Pasta` |
| `ren` ou `rename` | Renomeia um arquivo ou pasta | `ren antigo.txt novo.txt` |
| `type` | Mostra o conteúdo de um arquivo de texto | `type notas.txt` |
| `fc` | Compara o conteúdo de dois arquivos | `fc arquivo1.txt arquivo2.txt` |
| `attrib` | Mostra ou altera atributos de arquivo (oculto, somente leitura, etc.) | `attrib +h arquivo.txt` |

---

## 5. Informações do sistema

| Comando | Função |
|---|---|
| `systeminfo` | Exibe informações detalhadas do sistema operacional e hardware |
| `hostname` | Mostra o nome do computador |
| `whoami` | Mostra o usuário atualmente logado |
| `ver` | Mostra a versão do Windows |
| `tasklist` | Lista todos os processos em execução |
| `taskkill` | Encerra um processo | 
| `driverquery` | Lista os drivers instalados |
| `wmic` | Ferramenta de consulta avançada ao sistema (WMI) |

Exemplos com `taskkill`:
```
taskkill /IM notepad.exe /F
taskkill /PID 1234 /F
```

---

## 6. Rede

| Comando | Função |
|---|---|
| `ipconfig` | Mostra as configurações de rede (IP, gateway, DNS) |
| `ipconfig /all` | Mostra detalhes completos de rede |
| `ipconfig /flushdns` | Limpa o cache de DNS |
| `ping` | Testa a conectividade com um endereço | `ping google.com` |
| `tracert` | Rastreia o caminho até um destino | `tracert google.com` |
| `netstat` | Mostra conexões de rede ativas | `netstat -an` |
| `nslookup` | Consulta informações de DNS de um domínio | `nslookup google.com` |
| `netsh` | Configura interfaces de rede (avançado) | `netsh wlan show profiles` |
| `getmac` | Mostra o endereço MAC das interfaces de rede | |

---

## 7. Gerenciamento de disco

| Comando | Função |
|---|---|
| `chkdsk` | Verifica e corrige erros no disco | `chkdsk C: /f` |
| `diskpart` | Ferramenta avançada de particionamento (abre console próprio) | |
| `format` | Formata uma unidade | `format D: /FS:NTFS` |
| `vol` | Mostra o rótulo e número de série do volume | `vol C:` |
| `label` | Altera o rótulo do disco | `label C: MeuDisco` |
| `tree` | Mostra a estrutura de pastas em formato de árvore | `tree /F` |

---

## 8. Usuários e permissões

| Comando | Função |
|---|---|
| `net user` | Lista ou gerencia contas de usuário | `net user` |
| `net user [nome] [senha] /add` | Cria um novo usuário | |
| `net localgroup` | Lista ou gerencia grupos locais | `net localgroup administradores` |
| `runas` | Executa um programa como outro usuário | `runas /user:Administrador cmd` |
| `icacls` | Exibe/modifica permissões (ACL) de arquivos e pastas (avançado) | |

---

## 9. Variáveis e ambiente

| Comando | Função |
|---|---|
| `set` | Lista ou define variáveis de ambiente da sessão | `set NOME=Valor` |
| `echo %NOME%` | Exibe o valor de uma variável | |
| `echo %PATH%` | Mostra o PATH do sistema | |
| `setx` | Define variável de ambiente permanente | `setx NOME Valor` |
| `path` | Mostra ou define o PATH da sessão atual | |

---

## 10. Scripts em lote (Batch / .bat)

O CMD executa scripts `.bat`, permitindo automatizar sequências de comandos.

```bat
@echo off
echo Iniciando backup...
xcopy C:\Dados D:\Backup /E /H /Y
echo Backup concluído!
pause
```

Elementos comuns em scripts `.bat`:

| Elemento | Função |
|---|---|
| `@echo off` | Oculta os comandos sendo executados, mostrando só a saída |
| `echo` | Exibe uma mensagem na tela |
| `pause` | Pausa a execução até o usuário pressionar uma tecla |
| `rem` | Comentário (não executado) |
| `if` / `else` | Estrutura condicional |
| `for` | Estrutura de repetição |
| `goto` / `:label` | Desvia a execução para um rótulo específico |
| `call` | Chama outro script .bat |
| `%1`, `%2`... | Parâmetros passados ao script |

Exemplo de `for` percorrendo arquivos:
```bat
for %%f in (*.txt) do echo %%f
```

Exemplo de `if`:
```bat
if exist arquivo.txt (
    echo O arquivo existe.
) else (
    echo O arquivo não existe.
)
```

---

## 11. Redirecionamento e pipes (avançado)

| Operador | Função | Exemplo |
|---|---|---|
| `>` | Redireciona a saída para um arquivo (sobrescreve) | `dir > lista.txt` |
| `>>` | Redireciona a saída para um arquivo (anexa) | `dir >> lista.txt` |
| `<` | Usa um arquivo como entrada | `sort < dados.txt` |
| `\|` | Encadeia a saída de um comando como entrada de outro (pipe) | `dir \| find "txt"` |
| `&` | Executa comandos em sequência, independente do resultado | `cd Docs & dir` |
| `&&` | Executa o próximo comando apenas se o anterior tiver sucesso | `mkdir Nova && cd Nova` |
| `\|\|` | Executa o próximo comando apenas se o anterior falhar | `ping site.com \|\| echo Falhou` |

---

## 12. Comandos avançados úteis

| Comando | Função |
|---|---|
| `find` | Busca uma string dentro de arquivos de texto | `find "erro" log.txt` |
| `findstr` | Busca com suporte a expressões regulares (mais poderoso que `find`) | `findstr /i "erro" log.txt` |
| `sort` | Ordena o conteúdo de um arquivo ou saída | `sort arquivo.txt` |
| `sc` | Gerencia serviços do Windows | `sc query wuauserv` |
| `shutdown` | Desliga, reinicia ou agenda desligamento | `shutdown /r /t 0` |
| `schtasks` | Cria e gerencia tarefas agendadas | `schtasks /create /tn "Backup" /tr "backup.bat" /sc daily /st 08:00` |
| `powercfg` | Gerencia configurações de energia | `powercfg /list` |
| `assoc` | Mostra/altera associações de tipos de arquivo | `assoc .txt` |
| `ftype` | Mostra/altera o programa associado a um tipo de arquivo | |
| `wsl` | Abre o Windows Subsystem for Linux (se instalado) | `wsl` |
| `powershell` | Abre o PowerShell a partir do CMD | `powershell` |

---

## 13. Dicas rápidas

- Use aspas em caminhos com espaço: `cd "Meus Documentos"`
- `cls` limpa a tela mas não apaga o histórico de comandos (ainda dá para usar `↑`)
- `help [comando]` ou `[comando] /?` mostra a ajuda detalhada de qualquer comando (ex.: `xcopy /?`)
- Para copiar texto do CMD: selecione com o mouse e pressione Enter (ou `Ctrl+C` em versões mais novas)
- O CMD não é case-sensitive para comandos e caminhos

---

## 14. Próximos passos sugeridos

- Praticar criando pequenos scripts `.bat` de automação
- Explorar o **PowerShell**, que é o sucessor mais moderno e poderoso do CMD
- Estudar `robocopy` e `schtasks` para rotinas de backup automatizado
