# 🍌 BananaBot — Platform LinkTree

Each platform has a single, clear role. Nothing overlaps.

---

## Discord
- **Role:** BananaBot's front door — where users interact
- **Developer Portal:** https://discord.com/developers/applications
- **Tasks:** Bot settings / OAuth2 invite URL
- **Do NOT store here:** Bot Token / Client Secret

---

## Replit
- **Role:** BananaBot's laboratory — where code runs
- **Tasks:** Run and iterate on the bot
- **Secrets to add:** Bot Token / API Keys
- **Rule:** Never hardcode secrets in source files

---

## GitHub (this repo)
- **Role:** Public blueprint — design docs and safe configuration
- **Store here:** README / docs / `.env.example`
- **Do NOT store here:** `.env` / tokens / secret files

---

## Pinata
- **Role:** IPFS vault — permanent decentralized storage
- **Store here:** BananaMoon images / BananaBot icon / NFT metadata
- **Do NOT store here:** JWT / API Secret (use Secrets managers only)

---

## Notion
- **Role:** Mission control — process notes, decision logs, YAML templates
- **Store here:** Setup guides / judgment logs / LinkTree reference
- **Rule:** No secret values in page body text

---

## Information Security Tiers

| Tier | Examples | Where it lives |
|------|----------|----------------|
| ✅ Public | Project name, README, docs, `.env.example` variable names | GitHub (public) |
| ⚠️ Careful | Application ID, Public Key, OAuth2 invite URL | GitHub Secrets / Replit Secrets |
| 🔒 Never public | Bot Token, Client Secret, OpenAI Key, Pinata JWT | Replit Secrets / GitHub Secrets ONLY |
