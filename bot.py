from twitchio.ext import commands
from modules.config import get_config
from modules.input_handler import InputHandler

config = get_config(__file__)

class Bot(commands.Bot):
    """
        Class to control chat interaction
    """
    def __init__(self):
        super().__init__(token=config['token'], prefix=config['prefix'], initial_channels=config['channels'])
        self.input_handler = InputHandler()

    async def event_ready(self):
        print(f'SNES bot started...')


    @commands.command()
    async def test(self, ctx: commands.Context):
        """
            Test chat communication
        """
        await ctx.send(f'Tested, {ctx.author.name}!')


    @commands.command()
    async def right(self, ctx: commands.Context):
        """
            Send right command to emulator
        """
        self.input_handler.right()


    @commands.command()
    async def left(self, ctx: commands.Context):
        """
            Send left command to emulator
        """
        self.input_handler.left()


    @commands.command()
    async def up(self, ctx: commands.Context):
        """
            Send up command to emulator
        """
        self.input_handler.up()


    @commands.command()
    async def down(self, ctx: commands.Context):
        """
            Send down command to emulator
        """
        self.input_handler.down()


    @commands.command()
    async def a(self, ctx: commands.Context):
        """
            Send A command to emulator
        """
        self.input_handler.a()


    @commands.command()
    async def b(self, ctx: commands.Context):
        """
            Send B command to emulator
        """
        self.input_handler.b()


    @commands.command()
    async def x(self, ctx: commands.Context):
        """
            Send X command to emulator
        """
        self.input_handler.x()


    @commands.command()
    async def y(self, ctx: commands.Context):
        """
            Send Y command to emulator
        """
        self.input_handler.y()

if __name__ == '__main__':
    bot = Bot()
    bot.run()