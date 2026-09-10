# PowerShell — Guia do Básico ao Avançado

## 1. O que é o PowerShell

O **PowerShell** é o shell e linguagem de script mais moderno do Windows, sucessor do CMD. Diferente do CMD, ele trabalha com **objetos** (não apenas texto), o que permite filtrar, ordenar e manipular dados de forma muito mais poderosa.

Para abrir:
- Atalho `Win + X` → "Windows PowerShell" ou "Terminal"
- Pesquise "PowerShell" no menu Iniciar
- Para abrir como Administrador: clique com botão direito → "Executar como administrador"
- A partir do CMD: digite `powershell`

Há duas versões principais:
- **Windows PowerShell** (5.1) — vem embutido no Windows
- **PowerShell 7+** (multiplataforma, mais moderno) — instalado separadamente

---

## 2. Atalhos úteis do teclado

| Atalho | Função |
|---|---|
| `Tab` | Autocompletar comando, parâmetro ou caminho |
| `Shift + Tab` | Navegar para trás nas sugestões de autocompletar |
| `↑` / `↓` | Navegar pelo histórico de comandos |
| `Ctrl + R` | Buscar no histórico de comandos |
| `Ctrl + C` | Cancelar comando em execução |
| `Ctrl + L` | Limpar a tela (equivalente a `cls`) |
| `Ctrl + Home` / `Ctrl + End` | Mover cursor para início/fim da linha |
| `F7` | Mostrar histórico de comandos em um menu |
| `Alt + .` | Insere o último argumento do comando anterior |

---

## 3. Sintaxe básica: Verbo-Substantivo

Os comandos do PowerShell são chamados **cmdlets** e seguem o padrão `Verbo-Substantivo`:

| Cmdlet | Função |
|---|---|
| `Get-Help` | Mostra ajuda sobre um comando |
| `Get-Command` | Lista comandos disponíveis |
| `Get-Member` | Mostra propriedades e métodos de um objeto |
| `Get-Process` | Lista processos em execução |
| `Get-Service` | Lista serviços do Windows |

Exemplo de ajuda:
```powershell
Get-Help Get-Process -Examples
Get-Help Get-Process -Full
```

---

## 4. Navegação e arquivos

| Comando | Equivalente no CMD | Função |
|---|---|---|
| `Get-ChildItem` (alias `dir`, `ls`) | `dir` | Lista arquivos e pastas |
| `Set-Location` (alias `cd`) | `cd` | Muda o diretório atual |
| `Get-Location` (alias `pwd`) | `cd` (sem args) | Mostra o diretório atual |
| `New-Item` | `mkdir` / `md` | Cria arquivo ou pasta |
| `Remove-Item` (alias `rm`, `del`) | `del` / `rmdir` | Remove arquivo ou pasta |
| `Copy-Item` (alias `cp`, `copy`) | `copy` | Copia arquivos/pastas |
| `Move-Item` (alias `mv`, `move`) | `move` | Move ou renomeia |
| `Rename-Item` | `ren` | Renomeia um item |
| `Get-Content` (alias `cat`, `type`) | `type` | Mostra conteúdo de um arquivo |
| `Set-Content` / `Add-Content` | — | Escreve/adiciona conteúdo a um arquivo |
| `Clear-Host` (alias `cls`) | `cls` | Limpa a tela |

Exemplos:
```powershell
New-Item -Path "Projetos" -ItemType Directory
New-Item -Path "notas.txt" -ItemType File
Copy-Item "origem.txt" "destino.txt"
Get-ChildItem -Recurse -Filter *.txt
```

---

## 5. Trabalhando com objetos (o diferencial do PowerShell)

No PowerShell, a saída de um comando é um **objeto**, não apenas texto — por isso é possível filtrar e manipular dados com muito mais precisão.

| Cmdlet | Função |
|---|---|
| `Where-Object` (alias `?`) | Filtra objetos por condição |
| `Select-Object` (alias `select`) | Seleciona propriedades específicas |
| `Sort-Object` (alias `sort`) | Ordena objetos |
| `ForEach-Object` (alias `%`) | Executa uma ação para cada item |
| `Group-Object` | Agrupa itens por uma propriedade |
| `Measure-Object` | Calcula contagem, soma, média, etc. |

Exemplos:
```powershell
Get-Process | Where-Object { $_.CPU -gt 100 }
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
Get-ChildItem | Where-Object { $_.Extension -eq ".txt" }
Get-ChildItem | Measure-Object -Property Length -Sum
```

O `$_` representa o objeto atual dentro do pipeline.

---

## 6. Variáveis

| Sintaxe | Função |
|---|---|
| `$nome = "valor"` | Cria uma variável |
| `$nome` | Exibe o valor da variável |
| `$env:NOME` | Acessa uma variável de ambiente |
| `Get-Variable` | Lista variáveis da sessão |
| `Remove-Variable` | Remove uma variável |

Exemplo:
```powershell
$nome = "Maria"
$idade = 30
Write-Host "Nome: $nome, Idade: $idade"
```

Tipos são inferidos automaticamente, mas também podem ser definidos:
```powershell
[int]$numero = 10
[string]$texto = "Olá"
```

---

## 7. Estruturas de controle

### Condicionais
```powershell
if ($idade -ge 18) {
    Write-Host "Maior de idade"
} elseif ($idade -eq 17) {
    Write-Host "Quase lá"
} else {
    Write-Host "Menor de idade"
}
```

### Operadores de comparação (diferentes do CMD!)

| Operador | Significado |
|---|---|
| `-eq` | igual |
| `-ne` | diferente |
| `-gt` | maior que |
| `-lt` | menor que |
| `-ge` | maior ou igual |
| `-le` | menor ou igual |
| `-like` | comparação com curinga (`*`) |
| `-match` | comparação com regex |
| `-and`, `-or`, `-not` | operadores lógicos |

### Laços de repetição
```powershell
for ($i = 0; $i -lt 5; $i++) {
    Write-Host $i
}

foreach ($item in Get-ChildItem) {
    Write-Host $item.Name
}

$i = 0
while ($i -lt 5) {
    Write-Host $i
    $i++
}
```

### Switch
```powershell
switch ($dia) {
    "Seg" { "Segunda-feira" }
    "Ter" { "Terça-feira" }
    default { "Dia não reconhecido" }
}
```

---

## 8. Funções

```powershell
function Saudacao {
    param(
        [string]$Nome = "Visitante"
    )
    Write-Host "Olá, $Nome!"
}

Saudacao -Nome "João"
```

Funções podem retornar valores e aceitar múltiplos parâmetros tipados, com valores padrão e obrigatoriedade (`Mandatory`).

---

## 9. Rede

| Cmdlet | Função | Equivalente CMD |
|---|---|---|
| `Test-Connection` | Testa conectividade (ping) | `ping` |
| `Get-NetIPAddress` | Mostra endereços IP | `ipconfig` |
| `Get-NetIPConfiguration` | Configuração de rede detalhada | `ipconfig /all` |
| `Resolve-DnsName` | Consulta DNS | `nslookup` |
| `Test-NetConnection` | Testa conexão a uma porta/host específico | `tracert` / `telnet` |
| `Invoke-WebRequest` (alias `iwr`) | Faz requisições HTTP | — |
| `Invoke-RestMethod` (alias `irm`) | Faz requisições a APIs REST | — |

Exemplo:
```powershell
Test-NetConnection -ComputerName google.com -Port 443
Invoke-RestMethod -Uri "https://api.exemplo.com/dados"
```

---

## 10. Processos e serviços

| Cmdlet | Função |
|---|---|
| `Get-Process` | Lista processos em execução |
| `Stop-Process` | Encerra um processo |
| `Start-Process` | Inicia um programa/processo |
| `Get-Service` | Lista serviços do Windows |
| `Start-Service` / `Stop-Service` | Inicia/para um serviço |
| `Restart-Service` | Reinicia um serviço |

Exemplos:
```powershell
Get-Process notepad | Stop-Process
Start-Process "notepad.exe"
Get-Service | Where-Object { $_.Status -eq "Running" }
```

---

## 11. Gerenciamento do sistema

| Cmdlet | Função |
|---|---|
| `Get-ComputerInfo` | Informações detalhadas do sistema |
| `Get-EventLog` / `Get-WinEvent` | Consulta logs de eventos do Windows |
| `Get-Disk` / `Get-Volume` | Informações sobre discos e volumes |
| `Get-LocalUser` | Lista usuários locais |
| `Get-LocalGroup` | Lista grupos locais |
| `Restart-Computer` | Reinicia o computador |
| `Stop-Computer` | Desliga o computador |

---

## 12. Módulos (equivalente às bibliotecas do Python)

| Comando | Função |
|---|---|
| `Get-Module` | Lista módulos carregados |
| `Get-Module -ListAvailable` | Lista todos os módulos disponíveis |
| `Import-Module` | Carrega um módulo |
| `Install-Module` | Instala um módulo da PowerShell Gallery |
| `Find-Module` | Busca módulos disponíveis online |

Exemplo:
```powershell
Install-Module -Name Az -Scope CurrentUser
Import-Module Az
```

---

## 13. Scripts (.ps1)

Scripts do PowerShell usam a extensão `.ps1`.

```powershell
# backup.ps1
param(
    [string]$Origem = "C:\Dados",
    [string]$Destino = "D:\Backup"
)

Write-Host "Iniciando backup de $Origem para $Destino..."
Copy-Item -Path $Origem -Destination $Destino -Recurse -Force
Write-Host "Backup concluído!"
```

Executar:
```powershell
.\backup.ps1
```

### Política de execução
Por padrão, o Windows bloqueia a execução de scripts por segurança. Para verificar e alterar:
```powershell
Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 14. Redirecionamento, pipes e tratamento de erros

| Operador/Cmdlet | Função | Exemplo |
|---|---|---|
| `\|` | Encadeia comandos (pipeline de objetos) | `Get-Process \| Sort-Object CPU` |
| `>` | Redireciona saída para arquivo (sobrescreve) | `Get-Process > lista.txt` |
| `>>` | Redireciona saída para arquivo (anexa) | `Get-Process >> lista.txt` |
| `try / catch / finally` | Tratamento de erros | veja abaixo |
| `-ErrorAction` | Controla o comportamento em caso de erro | `Get-Item arquivo.txt -ErrorAction SilentlyContinue` |

```powershell
try {
    Get-Item "arquivo_inexistente.txt" -ErrorAction Stop
} catch {
    Write-Host "Erro: $($_.Exception.Message)"
} finally {
    Write-Host "Fim da tentativa."
}
```

---

## 15. Comandos avançados úteis

| Cmdlet | Função |
|---|---|
| `Get-Alias` | Lista todos os apelidos (aliases) de comandos |
| `New-Alias` | Cria um apelido personalizado |
| `ConvertTo-Json` / `ConvertFrom-Json` | Converte objetos de/para JSON |
| `Export-Csv` / `Import-Csv` | Exporta/importa dados em CSV |
| `Select-String` | Busca texto em arquivos (equivalente ao `findstr`, com regex) |
| `Compare-Object` | Compara duas coleções de objetos |
| `Invoke-Command` | Executa comandos remotamente (PowerShell Remoting) |
| `Get-Job` / `Start-Job` | Executa e gerencia tarefas em segundo plano |
| `Register-ScheduledTask` | Cria tarefas agendadas (equivalente ao `schtasks`) |

Exemplos:
```powershell
Get-Process | Export-Csv -Path "processos.csv" -NoTypeInformation
Select-String -Path "log.txt" -Pattern "erro"
Get-Process | ConvertTo-Json
```

---

## 16. Dicas rápidas

- Use `Get-Command -Verb Get` para ver todos os cmdlets que começam com "Get"
- `$_.PropertyName` acessa propriedades do objeto atual no pipeline
- O PowerShell não é case-sensitive
- `cls`, `dir`, `copy` e outros comandos do CMD funcionam como *aliases* de cmdlets do PowerShell
- Use `Get-Member` para descobrir quais propriedades e métodos um objeto tem: `Get-Process | Get-Member`
- O ISE (Integrated Scripting Environment) e o VS Code (com extensão PowerShell) são ótimos para escrever scripts maiores

---

## 17. Próximos passos sugeridos

- Praticar pipelines combinando `Where-Object`, `Sort-Object` e `Select-Object`
- Escrever pequenos scripts `.ps1` de automação de tarefas do dia a dia
- Explorar módulos específicos (ex.: `Az` para Azure, `ActiveDirectory` para AD)
- Estudar PowerShell Remoting (`Invoke-Command`, `Enter-PSSession`) para administração remota
