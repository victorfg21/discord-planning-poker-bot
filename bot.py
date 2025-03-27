import discord
from discord.ext import commands
from discord.ui import View, Button, Modal, TextInput

TOKEN = "MY_TOKEN"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

votes = {}
active_round = False

class VoteView(View):
    def __init__(self):
        super().__init__()
        options = {
            "0.5h ⏳": "0.5h",
            "1h 🕐": "1h",
            "2h 🕑": "2h",
            "4h 🕓": "4h",
            "8h 🕗": "8h",
            "16h 🕘": "16h",
            "❓": "?"
        }
        for emoji, value in options.items():
            self.add_item(VoteButton(emoji, value))
        self.add_item(CustomVoteButton())

class VoteButton(Button):
    def __init__(self, label, value):
        super().__init__(style=discord.ButtonStyle.primary, label=label)
        self.value = value

    async def callback(self, interaction: discord.Interaction):
        if not active_round:
            await interaction.response.send_message("⚠️ Nenhuma votação ativa!", ephemeral=True)
            return
        votes[interaction.user.id] = self.value
        await interaction.response.send_message(f"✅ Seu voto foi registrado: **{self.value}**", ephemeral=True)

class CustomVoteButton(Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.secondary, label="Digite outra quantidade ⌨️")

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(CustomVoteModal())

class CustomVoteModal(Modal, title="Digite seu voto em horas"):
    custom_vote = TextInput(label="Quantidade de horas", placeholder="Exemplo: 3.5", required=True)

    async def on_submit(self, interaction: discord.Interaction):
        if not active_round:
            await interaction.response.send_message("⚠️ Nenhuma votação ativa!", ephemeral=True)
            return
        try:
            float(self.custom_vote.value)
            votes[interaction.user.id] = self.custom_vote.value
            await interaction.response.send_message(f"✅ Seu voto foi registrado: **{self.custom_vote.value}h**", ephemeral=True)
        except ValueError:
            await interaction.response.send_message("❌ Por favor, insira um número válido (ex: 3.5)", ephemeral=True)

@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

@bot.command()
async def pokerstart(ctx):
    global votes, active_round
    votes.clear()
    active_round = True
    view = VoteView()
    await ctx.send("📊 **Uma nova rodada de Planning Poker começou!**\nClique em um botão para votar ou digite um valor personalizado:", view=view)

@bot.command()
async def pokerresults(ctx):
    global active_round
    active_round = False

    if not votes:
        await ctx.send("⚠️ Nenhum voto foi registrado!")
        return

    result = []
    total_hours = 0
    vote_count = 0

    for user_id, vote in votes.items():
        user = await bot.fetch_user(user_id)
        result.append(f"**{user.name}**: {vote}")
        
        if vote != "?":
            try:
                hours = float(vote.rstrip("h"))
                total_hours += hours
                vote_count += 1
            except ValueError:
                pass

    result_text = "\n".join(result)
    
    if vote_count > 0:
        average_hours = total_hours / vote_count
        result_text += f"\n\n📈 **Média das horas:** {average_hours:.2f}h"
    else:
        result_text += "\n\n📈 **Média das horas:** Não calculada (sem votos numéricos)"

    await ctx.send(f"✅ **Resultados do Planning Poker:**\n{result_text}")

    if ctx.channel.last_message:
        view = VoteView()
        view.disable_all_items()
        await ctx.channel.last_message.edit(view=view)

bot.run(TOKEN)