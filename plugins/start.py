from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("YouTube", url="https://youtube.com")]

    ])
    welcomed = f"👋Salom <b>{message.from_user.first_name}</b>\n/help buyruģini yuboring"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
