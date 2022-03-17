

def get_name(ctx):
    if not ctx.author.nick:
        return ctx.author.name
    else:
        return ctx.author.nick
