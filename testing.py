import discord
from discord import app_commands
import requests
import json
intents = discord.Intents.all()
client = discord.Client(commands_prefix="/", intents=intents)
tree = app_commands.CommandTree(client)

response= requests.get("https://www.dnd5eapi.co/api/spells/acid-arrow")
data=response.json()
@tree.command(
    description="information for the acid arrow spell",
    name="acidarrow",
async def acid_arrow(interaction):
    await interaction.response.send_message(data["desc"][0])


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=)
    print("This is somewhere to be. This is all you have, but it's still something. Streets and sodium lights. The sky, the world. You're still alive.")


client.run("NTUyMTU5MzkzNTg0NTEzMDI0.GKCXJD.qUFNDz_qEvo3-hg-L6EnnQ8tRmULN-4EZ4o6IM")
