
<img src="https://github.com/wandrewtischlerx/alabin/blob/main/Aladdin.png?raw=true" alt="Alabin v1.0">

<h1>Alabin v1.0</h1>

---

Alabin é uma ferramenta poderosa para criação de shells reversas em PowerShell, projetada para profissionais de segurança e testes de penetração. Esta ferramenta gera um payload totalmente funcional e ofuscado em formato batch (.bat) que, quando executado, estabelece uma conexão reversa com o listener especificado. O código inclui verificação de conexão e interface amigável para garantir sucesso na implantação.

<h2>Instalação:</h2>

Nenhuma instalação é necessária. Basta executar o script Python:


<h2>Funcionalidades:</h2>

- Gera payload PowerShell ofuscado em base64
- Cria arquivo batch pronto para execução
- Verifica acessibilidade da porta antes de gerar o payload
- Interface intuitiva com validação de entrada
- Suporte para qualquer porta entre 1-65535
- Detecção automática de problemas de conexão

<h2>Como Usar:</h2>

1. Execute o script Python
2. Informe o IP do listener (seu IP)
3. Informe a porta do listener
4. O script testará a conectividade
5. Um arquivo .bat será gerado automaticamente
6. Execute o arquivo no alvo enquanto mantém um listener ativo

<h2>Requisitos:</h2>

- Python 3.x
- PowerShell no sistema alvo
- Conexão de rede entre as máquinas

<h2>Aviso Legal:</h2>

⚠️ Esta ferramenta deve ser usada APENAS para:
- Testes de penetração autorizados
- Pesquisa de segurança
- Educação em segurança cibernética

O uso não autorizado em sistemas que você não possui é ilegal.

<h2>Exemplo de Saída:</h2>

O script gera um arquivo batch contendo:
- Comando PowerShell ofuscado
- Configurações para execução silenciosa
- Payload codificado em base64

<h2>Contribuições:</h2>

Contribuições são bem-vindas! Para sugerir melhorias ou reportar problemas, por favor abra uma issue ou envie um pull request.

<h2>Licença:</h2>

Este projeto está licenciado sob a MIT License (https://opensource.org/licenses/MIT).

---

Desenvolvido por Wandrew Tischler
