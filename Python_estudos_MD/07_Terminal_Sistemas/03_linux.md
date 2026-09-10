# Linux — Guia do Básico ao Avançado

## 1. O que é o Linux

O **Linux** é um kernel (núcleo de sistema operacional) open-source, base de diversas distribuições (distros) como Ubuntu, Debian, Fedora, Arch e **Kali Linux**. É o sistema dominante em servidores, nuvem e, especialmente, em segurança ofensiva/defensiva.

O terminal (shell) mais comum é o **Bash**, mas existem outros como Zsh e Fish.

---

## 2. Estrutura de diretórios

| Diretório | Função |
|---|---|
| `/` | Raiz do sistema |
| `/home` | Pastas pessoais dos usuários |
| `/root` | Pasta pessoal do usuário root (administrador) |
| `/etc` | Arquivos de configuração do sistema |
| `/bin`, `/usr/bin` | Executáveis/programas básicos |
| `/var` | Dados variáveis: logs, cache, filas |
| `/var/log` | Logs do sistema |
| `/tmp` | Arquivos temporários (apagados ao reiniciar) |
| `/opt` | Programas de terceiros instalados manualmente |
| `/dev` | Arquivos que representam dispositivos (discos, portas) |
| `/proc` | Informações do kernel e processos em tempo real (virtual) |
| `/mnt`, `/media` | Pontos de montagem de dispositivos/discos externos |

---

## 3. Navegação e arquivos

| Comando | Função |
|---|---|
| `pwd` | Mostra o diretório atual |
| `ls` | Lista arquivos e pastas |
| `ls -la` | Lista tudo, incluindo ocultos, em formato detalhado |
| `cd <pasta>` | Muda de diretório |
| `cd ..` | Sobe um nível |
| `cd ~` | Vai para a home do usuário |
| `mkdir <pasta>` | Cria uma pasta |
| `mkdir -p a/b/c` | Cria pastas aninhadas de uma vez |
| `touch <arquivo>` | Cria um arquivo vazio (ou atualiza data de modificação) |
| `cp <origem> <destino>` | Copia arquivos |
| `cp -r <pasta> <destino>` | Copia pastas recursivamente |
| `mv <origem> <destino>` | Move ou renomeia |
| `rm <arquivo>` | Remove um arquivo |
| `rm -r <pasta>` | Remove pasta e conteúdo |
| `rm -rf <pasta>` | Remove forçado, sem confirmação — ⚠️ use com cuidado |
| `cat <arquivo>` | Mostra conteúdo do arquivo |
| `less <arquivo>` | Visualiza arquivo com rolagem (não carrega tudo na memória) |
| `head -n 10 <arquivo>` | Mostra as primeiras 10 linhas |
| `tail -n 10 <arquivo>` | Mostra as últimas 10 linhas |
| `tail -f <arquivo>` | Acompanha um arquivo em tempo real (ótimo para logs) |

---

## 4. Permissões de arquivos

O Linux usa um sistema de permissões para **dono (user)**, **grupo (group)** e **outros (others)**.

```
-rwxr-xr--  1 usuario grupo  4096 jul 16 10:00 script.sh
```

| Posição | Significado |
|---|---|
| `r` | Leitura (read) |
| `w` | Escrita (write) |
| `x` | Execução (execute) |
| `-` | Sem permissão |

Cada permissão também tem valor numérico: `r=4`, `w=2`, `x=1`.

| Comando | Função |
|---|---|
| `chmod 755 arquivo` | Define permissões (dono: rwx, grupo: r-x, outros: r-x) |
| `chmod +x script.sh` | Adiciona permissão de execução |
| `chmod -R 755 pasta/` | Aplica recursivamente |
| `chown usuario:grupo arquivo` | Muda o dono/grupo do arquivo |

---

## 5. Usuários e permissões administrativas

| Comando | Função |
|---|---|
| `whoami` | Mostra o usuário atual |
| `id` | Mostra UID, GID e grupos do usuário |
| `sudo <comando>` | Executa um comando como administrador (root) |
| `su <usuario>` | Troca de usuário |
| `su -` | Vira root |
| `adduser <nome>` | Cria um novo usuário |
| `passwd <usuario>` | Altera senha de um usuário |
| `usermod -aG <grupo> <usuario>` | Adiciona usuário a um grupo |
| `deluser <usuario>` | Remove um usuário |

---

## 6. Processos

| Comando | Função |
|---|---|
| `ps aux` | Lista todos os processos em execução |
| `top` | Monitor de processos em tempo real |
| `htop` | Versão mais amigável do `top` (precisa instalar) |
| `kill <PID>` | Encerra um processo pelo ID |
| `kill -9 <PID>` | Força o encerramento |
| `killall <nome>` | Mata todos os processos com aquele nome |
| `<comando> &` | Executa em segundo plano |
| `jobs` | Lista processos em segundo plano da sessão atual |
| `fg` / `bg` | Traz para primeiro plano / envia para segundo plano |
| `nohup <comando> &` | Executa um processo que continua mesmo após fechar o terminal |

---

## 7. Pacotes (gerenciamento depende da distro)

| Distro | Gerenciador | Exemplos |
|---|---|---|
| Debian/Ubuntu/Kali | `apt` | `sudo apt update && sudo apt upgrade`, `sudo apt install nmap` |
| Fedora/RHEL | `dnf` / `yum` | `sudo dnf install nmap` |
| Arch | `pacman` | `sudo pacman -S nmap` |

Outros comandos úteis:
```bash
apt search <pacote>       # busca um pacote
apt remove <pacote>       # remove um pacote
apt autoremove            # limpa dependências não usadas
dpkg -l                   # lista pacotes instalados (Debian-based)
```

---

## 8. Redirecionamento e pipes

| Operador | Função | Exemplo |
|---|---|---|
| `>` | Redireciona saída (sobrescreve) | `ls > lista.txt` |
| `>>` | Redireciona saída (anexa) | `ls >> lista.txt` |
| `<` | Usa arquivo como entrada | `sort < dados.txt` |
| `\|` | Encadeia comandos | `cat log.txt \| grep erro` |
| `2>` | Redireciona erros | `comando 2> erros.txt` |
| `&>` | Redireciona saída E erros | `comando &> tudo.txt` |
| `&&` | Executa se o anterior teve sucesso | `mkdir x && cd x` |
| `\|\|` | Executa se o anterior falhou | `ping site \|\| echo "falhou"` |

---

## 9. Busca e manipulação de texto

| Comando | Função |
|---|---|
| `grep "termo" arquivo` | Busca uma string em um arquivo |
| `grep -r "termo" pasta/` | Busca recursivamente em uma pasta |
| `grep -i` | Busca ignorando maiúsculas/minúsculas |
| `grep -v` | Mostra linhas que NÃO contém o termo |
| `find / -name "arquivo.txt"` | Busca arquivos pelo nome |
| `find . -type f -mtime -1` | Busca arquivos modificados no último dia |
| `locate <arquivo>` | Busca rápida usando índice pré-construído |
| `which <comando>` | Mostra o caminho do executável de um comando |
| `sed 's/antigo/novo/g' arquivo` | Substitui texto em um arquivo (stream editor) |
| `awk '{print $1}' arquivo` | Processa texto por colunas |
| `sort arquivo` | Ordena linhas |
| `uniq` | Remove linhas duplicadas consecutivas |
| `wc -l arquivo` | Conta linhas de um arquivo |
| `cut -d "," -f1 arquivo.csv` | Extrai uma coluna de um CSV |

---

## 10. Rede

| Comando | Função |
|---|---|
| `ip a` | Mostra interfaces de rede e IPs (substitui o antigo `ifconfig`) |
| `ping <host>` | Testa conectividade |
| `curl <url>` | Faz requisições HTTP direto do terminal |
| `wget <url>` | Baixa arquivos da web |
| `ss -tulnp` | Mostra portas e conexões abertas (substitui o antigo `netstat`) |
| `netstat -tulnp` | Versão clássica do comando acima |
| `traceroute <host>` | Rastreia o caminho até um destino |
| `dig <dominio>` | Consulta DNS detalhada |
| `nslookup <dominio>` | Consulta DNS simples |
| `scp arquivo usuario@host:/destino` | Copia arquivo para outra máquina via SSH |
| `ssh usuario@host` | Conecta a outra máquina remotamente |

---

## 11. Compactação

| Comando | Função |
|---|---|
| `tar -czvf arquivo.tar.gz pasta/` | Compacta uma pasta (c=criar, z=gzip, v=verbose, f=arquivo) |
| `tar -xzvf arquivo.tar.gz` | Descompacta |
| `zip -r arquivo.zip pasta/` | Compacta em .zip |
| `unzip arquivo.zip` | Descompacta .zip |

---

## 12. Variáveis de ambiente e shell

| Comando | Função |
|---|---|
| `echo $VARIAVEL` | Mostra o valor de uma variável |
| `export VARIAVEL=valor` | Define uma variável de ambiente |
| `echo $PATH` | Mostra os diretórios onde o sistema busca executáveis |
| `env` | Lista todas as variáveis de ambiente |
| `alias ll='ls -la'` | Cria um atalho para um comando |
| `~/.bashrc` | Arquivo de configuração do shell (aliases, variáveis, etc.) |
| `source ~/.bashrc` | Recarrega as configurações do shell sem reiniciar |

---

## 13. Scripts Bash

```bash
#!/bin/bash
# backup.sh

ORIGEM="/home/usuario/dados"
DESTINO="/mnt/backup"

echo "Iniciando backup..."
cp -r "$ORIGEM" "$DESTINO"
echo "Backup concluído!"
```

Tornar executável e rodar:
```bash
chmod +x backup.sh
./backup.sh
```

Estruturas de controle:
```bash
# Condicional
if [ -f "arquivo.txt" ]; then
    echo "Arquivo existe"
else
    echo "Arquivo não existe"
fi

# Laço for
for i in 1 2 3; do
    echo "Número: $i"
done

# Laço while
contador=0
while [ $contador -lt 5 ]; do
    echo $contador
    contador=$((contador+1))
done
```

---

## 14. Discos e armazenamento

| Comando | Função |
|---|---|
| `df -h` | Mostra espaço em disco (formato legível) |
| `du -sh <pasta>` | Mostra tamanho de uma pasta |
| `mount` | Lista/monta sistemas de arquivos |
| `umount <ponto>` | Desmonta um dispositivo |
| `lsblk` | Lista discos e partições |
| `fdisk -l` | Detalha partições (requer sudo) |

---

## 15. Logs e monitoramento (avançado)

| Comando | Função |
|---|---|
| `journalctl` | Mostra logs do systemd |
| `journalctl -u <serviço>` | Logs de um serviço específico |
| `journalctl -f` | Acompanha logs em tempo real |
| `systemctl status <serviço>` | Mostra status de um serviço |
| `systemctl start/stop/restart <serviço>` | Controla um serviço |
| `systemctl enable <serviço>` | Faz o serviço iniciar junto com o sistema |
| `dmesg` | Mostra mensagens do kernel (boot, hardware) |
| `cron` / `crontab -e` | Agenda tarefas recorrentes |

Exemplo de crontab (executa todo dia às 3h):
```
0 3 * * * /home/usuario/backup.sh
```

---

## 16. Boas práticas

- Sempre revise comandos com `sudo` e `rm -rf` antes de rodar — não há "lixeira"
- Prefira `cp`/`mv` com `-i` (interativo) quando estiver testando algo novo
- Use `man <comando>` para consultar o manual completo de qualquer comando
- Automatize tarefas repetitivas com scripts Bash e `cron`
- Mantenha o sistema atualizado (`apt update && apt upgrade`)

---

## 17. Próximos passos sugeridos

- Praticar pipelines combinando `grep`, `awk` e `sed`
- Escrever scripts Bash de automação simples
- Estudar `systemd` e gerenciamento de serviços
- Seguir para o arquivo de **Kali Linux**, que usa esta base para ferramentas de segurança ofensiva
