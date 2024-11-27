# ISMAEL - Discord Moderation Bot

Um bot simples para automação de moderação em servidores Discord. O ISMAEL pode banir, expulsar membros, limpar mensagens e gerenciar a interação com os membros de maneira eficaz.

## Funcionalidades

- **!ban [usuário]**: Bane um usuário do servidor.
- **!kick [usuário]**: Expulsa um usuário do servidor.
- **!clear [número]**: Apaga um número específico de mensagens no canal.
- **!regras**: Exibe as regras do servidor.
- **Boas-vindas automáticas**: Envia uma mensagem de boas-vindas para novos membros.

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ismael-bot.git
   cd ismael-bot
   ```

2. Instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Adicione seu token do bot no arquivo `bot.py`:
   - No arquivo `bot.py`, substitua `'SEU_TOKEN_AQUI'` pelo seu token do Discord.

   Exemplo:
   ```python
   bot.run('SEU_TOKEN_AQUI')
   ```

4. Execute o bot:
   ```bash
   python bot.py
   ```

## Comandos Disponíveis

- **!ban [usuário]**: Banir um usuário do servidor.
- **!kick [usuário]**: Expulsar um usuário do servidor.
- **!clear [número]**: Limpar as mensagens mais recentes no canal.
- **!regras**: Exibir as regras do servidor.

## Contribuindo

1. Faça um fork deste repositório.
2. Crie uma branch com a sua feature (`git checkout -b minha-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin minha-feature`).
5. Envie um pull request.

## Contato

- **E-mail**: blucasmoura21@gmail.com
- **GitHub**: https://github.com/Lluke-bit
