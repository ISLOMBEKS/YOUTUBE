from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"YouTube video linkini yuboring!"
    await message.reply_text(helptxt)
