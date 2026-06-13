# 🍌 BananaBot — Platform Link Tree

Each platform has a single, clear role. No overlap. No confusion.

---

## Discord

- **Role:** BananaBot's front door — where users interact
- **Portal:** [discord.com/developers/applications](https://discord.com/developers/applications)
- **Tasks:** Bot settings · OAuth2 invite URL · Server permissions
- **Keep private:** Bot Token · Client Secret · OAuth2 Secret

---

## Replit

- **Role:** Live experimental runtime
- **Tasks:** Run `Hello BananaBot` · Test commands · Iterate fast
- **Secrets tab:** Bot Token · API Key · Pinata JWT
- **Rule:** Never write secrets directly in code

---

## GitHub ← you are here

- **Role:** Public design docs and version-controlled specs
- **Contains:** README · docs · `.env.example`
- **Never contains:** `.env` · any token · any secret file
- **GitHub Secrets (Actions):**
  - `DISCORD_BOT_TOKEN`
  - `DISCORD_APPLICATION_ID`
  - `DISCORD_PUBLIC_KEY`
  - `OPENAI_API_KEY`
  - `PINATA_JWT`

---

## Pinata / IPFS

- **Role:** Permanent decentralized storage
- **Stores:** BananaMoon images · BananaBot icon · NFT metadata
- **Keep private:** Pinata JWT · Pinata API Secret

---

## Notion

- **Role:** Command center and decision log
- **Contains:** Setup notes · Judgment logs · Link tree · YAML templates
- **Rule:** No secret values in page body — ever

---

## Information Classification

### ✅ Safe to make public
- Project name and description
- README content
- docs structure
- Setup procedures
- Variable *names* in `.env.example`
- Secret *names* only (not values)

### ⚠️ Handle with care
- Discord Application ID
- Discord Public Key
- OAuth2 invite URL
- Bot configuration notes

> These can be public, but treat them carefully.  
> OK in GitHub Secrets / Replit Secrets.  
> Confirm paste destination when working on iPhone.

### 🔒 Never expose
- Bot Token
- Client Secret
- OAuth2 Secret
- OpenAI API Key
- GitHub Token
- Pinata JWT
- Pinata API Secret
- `.env` actual file

> Only in Replit Secrets or GitHub Secrets.  
> Never in Notion body. Never in code. Never in screenshots.
