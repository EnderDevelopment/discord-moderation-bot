import discord
from discord.ext import commands
from flask import Flask, render_template, request

app = Flask(__name__)

class Dashboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command()
        async def dashboard(self, ctx):
            await ctx.send('Dashboard is running at http://localhost:5000')

            @app.route('/')
            def home():
                return render_template('index.html')

                @app.route('/configure', methods=['POST'])
                def configure():
                    data = request.form
                    # Handle configuration data
                    return 'Configuration saved'

                    def setup(bot):
                        bot.add_cog(Dashboard(bot))
                        app.run(debug=True)
