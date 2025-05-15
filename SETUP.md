# ⚙️ Configuração do Telegram Bot

Este projeto contém o código-fonte de um bot simples do Telegram, feito com Python. Para executá-lo, você precisa criar seu próprio bot no Telegram e configurar o token de acesso.

---

## 📌 Etapa 1: Crie seu bot no Telegram com o BotFather

1. Abra o Telegram e procure por [@BotFather](https://t.me/BotFather)
2. Envie o comando: `/start`
3. Envie: `/newbot`
4. Dê um nome para o bot (exemplo: `MeuBot`)
5. Escolha um username (precisa terminar com `bot`, ex: `meu_bot_teste`)
6. Copie o token gerado. Ele terá esse formato:

```
123456789:ABCDefghIJKlmNOPQrstUVwxYZ
```

---

## 🔐 Etapa 2: Configure o token no Replit

1. Acesse seu projeto no [Replit](https://replit.com)
2. No menu esquerdo, clique em **Secrets** (ícone de cadeado)
3. Crie uma nova variável:
   - **Key**: `TELEGRAM_TOKEN`
   - **Value**: cole o token que recebeu do BotFather

---

## ✅ Pronto!

Agora é só clicar em **Run** no Replit e seu bot estará funcionando!

---

## ⚠️ Importante

O token nunca deve ser incluído diretamente no código (como em `main.py`). Use sempre variáveis de ambiente para garantir a segurança do seu projeto.

---

## 📁 Estrutura básica do projeto

```
telegram-bot/
├── main.py
├── README.md
└── SETUP.md  ← este arquivo
```
