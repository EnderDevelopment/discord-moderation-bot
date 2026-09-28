import discord
from discord.ext import commands

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.Cog.listener()
        async def on_message(self, message):
            if message.author == self.bot.user:
                return
                if 'badword' in message.content:
                    await message.delete()
                    await message.channel.send(f'{message.author.mention}, please avoid using inappropriate language.')

                    def setup(bot):
                        bot.add_cog(AutoMod(bot))
