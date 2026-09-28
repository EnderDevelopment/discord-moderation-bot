import discord
from discord.ext import commands
import sqlite3

class WarningSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect('warnings.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS warnings (
            user_id INTEGER,
            server_id INTEGER,
            warning TEXT,
            moderator_id INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        self.conn.commit()

        @commands.command()
        async def warn(self, ctx, member: discord.Member, *, reason):
            self.cursor.execute("INSERT INTO warnings (user_id, server_id, warning, moderator_id) VALUES (?, ?, ?, ?)", (member.id, ctx.guild.id, reason, ctx.author.id))
            self.conn.commit()
            await ctx.send(f'{member.mention} has been warned for: {reason}')

            @commands.command()
            async def warnings(self, ctx, member: discord.Member):
                self.cursor.execute("SELECT warning, moderator_id, timestamp FROM warnings WHERE user_id = ? AND server_id = ?", (member.id, ctx.guild.id))
                warnings = self.cursor.fetchall()
                if not warnings:
                    await ctx.send(f'{member.mention} has no warnings.')
                    return
                    embed = discord.Embed(title=f'Warnings for {member.name}', color=discord.Color.red())
                    for warning in warnings:
                        moderator = ctx.guild.get_member(warning[1])
                        embed.add_field(name=f'Moderator: {moderator.name}', value=f'Reason: {warning[0]}\nTimestamp: {warning[2]}', inline=False)
                        await ctx.send(embed=embed)

                        def setup(bot):
                            bot.add_cog(WarningSystem(bot))
