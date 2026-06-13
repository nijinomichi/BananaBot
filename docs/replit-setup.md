# 🍌 BananaBot — Replit Setup Guide

Step 4 of the minimum action plan: run Hello BananaBot on Replit.

---

## Prerequisites

- [ ] BananaBot invited to your Discord server (Step 3 done)
- [ ] Bot Token ready (stored nowhere except your memory or password manager)
- [ ] Replit account logged in

---

## Step 1 — Create a Replit Project

1. Go to [replit.com](https://replit.com)
2. Click **+ Create Repl**
3. Choose template: **Python**
4. Name it: `BananaBot`
5. Click **Create Repl**

---

## Step 2 — Add the Code

Option A — Import from GitHub (recommended):
1. In Replit, click **Import from GitHub**
2. Paste: `https://github.com/nijinomichi/BananaBot`
3. Replit will import `main.py` and `requirements.txt` automatically

Option B — Manual:
1. Copy the contents of `main.py` from this repo
2. Paste into the `main.py` file in Replit
3. Copy `requirements.txt` and paste into a new file by the same name

---

## Step 3 — Set the Secret

**This is the most important step. Never skip it.**

1. In Replit, click the 🔒 **Secrets** tab (left sidebar)
2. Click **+ New Secret**
3. Key: `DISCORD_BOT_TOKEN`
4. Value: paste your Bot Token here (and nowhere else)
5. Click **Add Secret**

> ⚠️ If you paste the token directly into `main.py`, stop.
> Delete it immediately. Tokens in code files are a security risk.

---

## Step 4 — Run

1. Click the green **▶ Run** button
2. Watch the console output
3. You should see:
   ```
   🍌 BananaBot is online as BananaBot#XXXX
      Connected to 1 server(s)
      Slash commands synced ✅
   ```
4. Go to your Discord server — BananaBot should appear **online**

---

## Step 5 — Test

In your Discord server, try:

| Command | Expected result |
|---|---|
| `/hello` | `🍌 Hello, [your name]! BananaBot is alive.` |
| `/ping` | `🏓 Pong! Latency: XXms` |
| `/banana` | A quantum banana appears 🍌 |
| `!hello` | Prefix command backup |

> Note: Slash commands (`/hello`) may take up to 1 hour to appear globally after first sync.
> They appear instantly in the server where the bot is present.

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `DISCORD_BOT_TOKEN is not set` | Add the token to Replit Secrets tab |
| Bot appears offline | Check Replit console for errors |
| Slash commands don't appear | Wait a few minutes; try `/` in the server |
| `Privileged Intents` error | Enable `Message Content Intent` in Discord Developer Portal → Bot tab |
| `discord.py` not found | Replit auto-installs from `requirements.txt`; try stopping and re-running |

---

## After Success

Once BananaBot responds in Discord:

1. ✅ Step 4 is complete
2. Next: expand commands (OpenAI integration, Pinata IPFS, etc.)
3. This repo is your public base — keep secrets out of it forever

---

*One step at a time. The quantum field rewards patience.*
