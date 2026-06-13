# 🍌 BananaBot — Discord Setup Guide

A minimal, non-destructive setup flow. One step at a time.

---

## Prerequisites

- [ ] Discord account with a server you own
- [ ] Access to [Discord Developer Portal](https://discord.com/developers/applications)
- [ ] Bot Token stored in Replit Secrets (not in this file)

---

## Step 1 — Confirm Bot Settings

1. Go to [discord.com/developers/applications](https://discord.com/developers/applications)
2. Open your BananaBot application
3. Confirm: name, icon, and description are set
4. Note your **Application ID** and **Public Key** (safe to record in Notion)
5. Under **Bot** tab: confirm bot user exists

---

## Step 2 — Create OAuth2 Invite URL

1. Go to **OAuth2 → URL Generator**
2. Scopes: `bot`
3. Bot Permissions: `Send Messages`, `Read Message History`, `Use Slash Commands`
4. Copy the generated URL
5. Paste it in Notion (URL itself is safe — it contains no secrets)

---

## Step 3 — Invite Bot to Your Server

1. Open the OAuth2 URL in your browser
2. Select your test server
3. Authorize
4. Confirm BananaBot appears in your server's member list

---

## Step 4 — Run Hello BananaBot on Replit

1. Open your Replit project
2. Add `DISCORD_BOT_TOKEN` to Secrets tab
3. Run the bot
4. Confirm: bot appears online in Discord
5. Send a test message or slash command

---

## Step 5 — Commit to GitHub

Only after Step 4 succeeds:

1. Confirm no secrets are in any file
2. Commit `README.md`, `docs/`, `.env.example`
3. Push to `main`

---

## What NOT to Do

- Do not regenerate Bot Token at midnight
- Do not implement complex OAuth2 code grant flows yet
- Do not paste Bot Token into Notion or GitHub body
- Do not automate everything at once
- Do not do long configuration sessions on iPhone

---

## GitHub Migration Checklist

- [ ] Bot Token is not in any file
- [ ] Client Secret is not in any file
- [ ] OpenAI API Key is not in any file
- [ ] Pinata JWT is not in any file
- [ ] No `.env` actual file committed
- [ ] Application ID / Public Key classified as "handle with care"
- [ ] Files to commit and Secrets to store are clearly separated
- [ ] You know exactly what to press next (only one action at a time)

---

*Next action when ready: go to Step 4 — Replit.*
