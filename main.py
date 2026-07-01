# 🍌 BananaBot — Causality Edition
# The world is already generated. Here we finally apply causality.
# Replit-ready Discord bot. Set DISCORD_BOT_TOKEN in Secrets. Never paste tokens here.

import os
import json
import time
import random
import discord
from discord.ext import commands

# ── Persistence ───────────────────────────────────────
# The world is generated once and never regenerated. Causality is written to disk.
WORLD_PATH = "world_state.json"

def load_world():
    """Load the persistent world, or generate it once if it does not exist."""
    if os.path.exists(WORLD_PATH):
        try:
            with open(WORLD_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    # The world is generated exactly once.
    return {
        "born_at": time.time(),
        "collapses": 0,
        "observers": {},
        "entanglement": None,
        "field_energy": 1.0,
        "log": [],
    }

def save_world():
    """Persist causality so it survives restarts. The world is never reset."""
    try:
        with open(WORLD_PATH, "w", encoding="utf-8") as f:
            json.dump(world, f, ensure_ascii=False, indent=2)
    except OSError:
        pass


# The world exists before any observer. Causality begins now.
world = load_world()


# ── Intents & Bot ──────────────────────────────────
intents = discord.Intents.default()
intents.message_content = True  # required to read message content

bot = commands.Bot(command_prefix="!", intents=intents)
# ── Events ──────────────────────────────────────
@bot.event
async def on_ready():
    print(f"🍌 BananaBot is online as {bot.user}")
    print(f"   Connected to {len(bot.guilds)} server(s)")
    print(f"   World age: {round(time.time() - world['born_at'])}s | collapses: {world['collapses']}")
    await bot.tree.sync()  # sync slash commands
    print("   Slash commands synced ✅")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

# ── Slash Commands ────────────────────────────────
@bot.tree.command(name="hello", description="Say hello to BananaBot 🍌")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"🍌 Hello, {interaction.user.display_name}! BananaBot is alive."
    )


@bot.tree.command(name="ping", description="Check if BananaBot is responding")
async def ping(interaction: discord.Interaction):
    latency_ms = round(bot.latency * 1000)
    await interaction.response.send_message(f"🏓 Pong! Latency: {latency_ms}ms")

@bot.tree.command(name="banana", description="Collapse the quantum field 🍌")
async def banana(interaction: discord.Interaction):
    uid = str(interaction.user.id)
    name = interaction.user.display_name

    # ── Apply causality ── the world already existed; now it is changed, irreversibly.
    world["collapses"] += 1
    world["observers"][uid] = world["observers"].get(uid, 0) + 1
    world["field_energy"] = round(world["field_energy"] * 0.98, 6)
    previous = world["entanglement"]
    world["entanglement"] = name

    n = world["observers"][uid]
    # The accumulated history bends the outcome: a fatigued field yields unstable harvests.
    spread = max(0.0, 1.0 - world["field_energy"])
    harvest = max(0, round(random.gauss(1, spread)))

    world["log"].append({"t": time.time(), "observer": name, "harvest": harvest})
    save_world()

    lines = [
        "🍌 *A banana condenses out of a field that was already there.*",
        f"> Global collapses so far: **{world['collapses']}**",
        f"> Your personal observations: **{n}**",
        f"> Field energy remaining: **{world['field_energy']:.3f}**",
    ]
    if previous and previous != name:
        lines.append(f"> You are now entangled with **{previous}**'s last observation.")
    lines.append(f"> You have received: **{harvest} Banana(s)**.")
    if world["field_energy"] < 0.85:
        lines.append("> ⚠️ The field is fatiguing. Causality accumulates; nothing resets.")

    await interaction.response.send_message("\n".join(lines))

@bot.tree.command(name="field", description="Observe the state of the world 🌀")
async def field(interaction: discord.Interaction):
    age = round(time.time() - world["born_at"])
    await interaction.response.send_message(
        "🌀 **World State**\n"
        f"> Age: {age}s (generated once, never regenerated)\n"
        f"> Total collapses: {world['collapses']}\n"
        f"> Unique observers: {len(world['observers'])}\n"
        f"> Field energy: {world['field_energy']:.3f}\n"
        f"> Last entangled observer: {world['entanglement'] or 'none yet'}"
    )


# ── Prefix Commands (backup) ──────────────────────────
@bot.command(name="hello")
async def hello_prefix(ctx):
    await ctx.send(f"🍌 Hello, {ctx.author.display_name}! BananaBot is alive.")


# ── Run ───────────────────────────────────────
if __name__ == "__main__":
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if not token:
        print("❌ DISCORD_BOT_TOKEN is not set.")
        print("   Go to Replit Secrets tab and add DISCORD_BOT_TOKEN.")
        raise SystemExit(1)
    bot.run(token)
