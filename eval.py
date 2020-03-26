import ast
import discord
from discord.ext import commands
forbidden = 'You\'re not allowed to use this command.'

def insert_returns(body):
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)
        
class Eval(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def eval(self, ctx, *, cmd):
        try:
            if ctx.author.id in [YOURID]:
                fn_name = '_eval_expr'

                cmd = cmd.strip('` ')

                cmd = '\n'.join(f"    {i}" for i in cmd.splitlines())

                body = f'async def {fn_name}():\n{cmd}'

                parsed = ast.parse(body)
                body = parsed.body[0].body

                insert_returns(body)

                env = {
                    'bot': ctx.bot,
                    'discord': discord,
                    'commands': commands,
                    'ctx': ctx,
                    '__import__': __import__
                }

                exec(compile(parsed, filename='<ast>', mode='exec'), env)

                result = (await eval(f'{fn_name}()', env))
                await ctx.send(result)
            else:
                await ctx.send(forbidden)

        except Exception as e:
            await ctx.send('```\n{}\n```'.format(type(e).__name__ + ': ' + str(e)))
    
def setup(client):
    client.add_cog(Eval(client))
