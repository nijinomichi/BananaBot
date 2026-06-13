# Discord Bot Setup Guide

Minimal steps to get BananaBot running from scratch.

---

## 1. Create the Application

1. Go to https://discord.com/developers/applications
2. Click **New Application** → name it `BananaBot`
3. Add icon and description under **General Information**
4. Note your **Application ID** and **Public Key** (these are safe to store in docs)

---

## 2. Create the Bot

1. Go to **Bot** tab
2. Click **Add Bot** → confirm
3. Under **Token**, click **Reset Token** → copy it
4. **Immediately** store the token in Replit Secrets as `DISCORD_BOT_TOKEN`
5. Never paste the token into any file, chat, or document

### Bot Permissions to enable:
- `Send Messages`
- `Use Slash Commands`
- `Read Message History`
- `Embed Links`

---

## 3. Generate OAuth2 Invite URL

1. Go to **OAuth2 → URL Generator**
2. Scopes: `bot` + `applications.commands`
3. Bot Permissions: select the ones from step 2
4. Copy the generated URL
5. Open it in a browser → select your server → Authorize

---

## 4. Verify Connection

After running the bot on Replit, you should see:

```
BananaBot is online as Bananabot#3512
Connected to 1 server(s)
Slash commands synced
```

If you see this, **Phase 1 is complete.** 🍌

---

## Security Checklist Before Any Commit

- [ ] Bot Token not in any source file
- [ ] Client Secret not in any source file
- [ ] OpenAI API Key not in any source file
- [ ] Pinata JWT not in any source file
- [ ] `.env` is in `.gitignore`
- [ ] Only `.env.example` (with placeholder values) is committed
