from twitchio.ext import commands
from modules.config import get_config

config = get_config(__file__)

class Bot(commands.Bot):
    """
        Class to control chat interaction
    """
    def __init__(self):
        super().__init__(token=config['token'], prefix=config['prefix'], initial_channels=config['channels'])

    async def event_ready(self):
        print(f'Bot connected...')

    @commands.command()
    async def test(self, ctx: commands.Context):
        """
            Test chat communication
        """
        await ctx.send(f'Tested, {ctx.author.name}!')
