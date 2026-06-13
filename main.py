# 🍌 BananaBot — Hello BananaBot
# Replit-ready minimal Discord bot
# Secrets: set DISCORD_BOT_TOKEN in Replit Secrets tab
# Never paste your token here.

import os
import discord
from discord.ext import commands

# ── Intents ────────────────────────────────────────────────
intents = discord.Intents.default()
intents.message_content = True  # required to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

# ── Events ─────────────────────────────────────────────────
@bot.event
async def on_ready():
    print(f"🍌 BananaBot is online as {bot.user}")
    print(f"   Connected to {len(bot.guilds)} server(s)")
    await bot.tree.sync()  # sync slash commands
    print("   Slash commands synced ✅")


@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    await bot.process_commands(message)


# ── Slash Commands ─────────────────────────────────────────
@bot.tree.command(name="hello", description="Say hello to BananaBot 🍌")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🍌 Hello, {interaction.user.display_name}! BananaBot is alive."
    )


@bot.tree.command(name="ping", description="Check if BananaBot is responding")
async def ping(interaction: discord.Interaction):
    latency_ms = round(bot.latency * 1000)
    await interaction.response.send_message(
        f"🏓 Pong! Latency: {latency_ms}ms"
    )


@bot.tree.command(name="banana", description="Receive a quantum banana 🍌")
async def banana(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🍌 *A banana materializes from the quantum field.*\n"
        "> The observer has collapsed the wave function.\n"
        "> You have received: **1 Banana**."
    )


# ── Prefix Commands (backup) ────────────────────────────────
@bot.command(name="hello")
async def hello_prefix(ctx):
    await ctx.send(f"🍌 Hello, {ctx.author.display_name}! BananaBot is alive.")


# ── Run ────────────────────────────────────────────────────
if __name__ == "__main__":
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        print("❌ DISCORD_BOT_TOKEN is not set.")
        print("   Go to Replit Secrets tab and add DISCORD_BOT_TOKEN.")
        raise SystemExit(1)
    bot.run(token)
