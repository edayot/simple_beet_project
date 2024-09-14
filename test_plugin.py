from beet import Context




def beet_default(ctx: Context):
    for function in ctx.data.functions:
        ctx.data.functions[function].prepend(f"# header {function}")