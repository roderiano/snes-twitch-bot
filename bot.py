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
        print(f'Starting...')

    async def event_ready(self):
        print('SNES bot started...')


    @commands.command()
    async def help(self, ctx: commands.Context):
        """
            Command list
        """
        prefix = config['prefix']
        await ctx.send(f'Hello, {ctx.author.name}!')
        
        for command in self.commands:
            if command != 'help':
                description = eval(f'Bot.{command}._callback').__doc__
                await ctx.send(f'{prefix}{command} -> {description}')


    @commands.command()
    async def r(self, ctx: commands.Context):
        """
            Send Right command to emulator
        """
        self.input_handler.right()


    @commands.command()
    async def l(self, ctx: commands.Context):
        """
            Send Left command to emulator
        """
        self.input_handler.left()


    @commands.command()
    async def u(self, ctx: commands.Context):
        """
            Send Up command to emulator
        """
        self.input_handler.up()


    @commands.command()
    async def d(self, ctx: commands.Context):
        """
            Send Down command to emulator
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