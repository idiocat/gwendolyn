from telegram.ext import ContextTypes
from database import api_request, organize

async def output(context: ContextTypes.DEFAULT_TYPE):
    job = context.job
    fonc, prop, amount, search_range, search_order = job.data

    if fonc == 'low':
        results = api_request.go_low(prop, amount)
    elif fonc == 'high':
        results = api_request.go_high(prop, amount)
    elif fonc == 'custom':
        results = api_request.go_custom(prop, search_range, search_order, amount)
    else:
        await context.bot.send_message(job.chat_id, text="Wait, what are we doing here?")
        return

    # await context.bot.send_message(job.chat_id, text=f"{len(results)}, {len(results[0])}")
    # await context.bot.send_message(job.chat_id, text=f"{results[0].get('target_name')}, {results[0].get('mass')}")
    
    try:
        results[0]
        for result in organize.organize(results):
            await context.bot.send_message(job.chat_id, text=result)
    except IndexError:
        await context.bot.send_message(job.chat_id, text="Apparently, there's nothing matching your request in the observable universe. Nothing that we know, at least.")