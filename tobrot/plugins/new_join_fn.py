#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import pyrogram

from tobrot import (
    AUTH_CHANNEL,
    LEECH_COMMAND,
    YTDL_COMMAND,
    GLEECH_COMMAND,
    TELEGRAM_LEECH_COMMAND_G,
    CANCEL_COMMAND_G,
    GET_SIZE_G,
    STATUS_COMMAND,
    SAVE_THUMBNAIL,
    CLEAR_THUMBNAIL,
    PYTDL_COMMAND_G,
    LOG_COMMAND
)


async def new_join_f(client, message):
    chat_type = message.chat.type
    if chat_type != "private":
        await message.reply_text(f"Current CHAT ID: <code>{message.chat.id}</code>")
        # leave chat
        await client.leave_chat(
            chat_id=message.chat.id,
            delete=True
        )
    # delete all other messages, except for AUTH_CHANNEL
    await message.delete(revoke=True)


async def help_message_f(client, message):
    # await message.reply_text("no one gonna help you 🤣🤣🤣🤣", quote=True)
    #channel_id = str(AUTH_CHANNEL)[4:]
    #message_id = 99
    # display the /help

    help_msg = f'''
> Available Commands

=> These commands should be used as a reply to a magnet link, a torrent link, or a direct link.

=>> Uploads to telegram.

/{LEECH_COMMAND}
/{LEECH_COMMAND} archive
/{LEECH_COMMAND} unzip
/{LEECH_COMMAND} unrar
/{LEECH_COMMAND} untar

=>> Uploads to cloud.

/{GLEECH_COMMAND}
/{GLEECH_COMMAND} archive
/{GLEECH_COMMAND} unzip
/{GLEECH_COMMAND} unrar
/{GLEECH_COMMAND} untar

=> These commands should be used as a reply to a telegram file. Uploads telegram files to cloud.

/{TELEGRAM_LEECH_COMMAND_G}
/{TELEGRAM_LEECH_COMMAND_G} unzip
/{TELEGRAM_LEECH_COMMAND_G} unrar
/{TELEGRAM_LEECH_COMMAND_G} untar

=> These commands should be used as a reply to a supported link.

/{YTDL_COMMAND} : Uploads to tg.
/{YTDL_COMMAND} gdrive : Upload to cloud.

=> These commands should be used as a reply to a youtube playlist link.

/{PYTDL_COMMAND_G} : Upload to telegram.
/{PYTDL_COMMAND_G} gdrive : Upload to cloud.

=> Extras

/{SAVE_THUMBNAIL} : Set thumbnail(logo) in doc only mode too.

/{CLEAR_THUMBNAIL} : Clear thumbnail(logo).

/{GET_SIZE_G} : This will give you total size of your destination folder in cloud.

/renewme : This will clear the remains of downloads which are not getting deleted after upload of the file or after /cancel command.

/{STATUS_COMMAND} : Get the status message.

/{CANCEL_COMMAND_G} : Cancel it !

/{LOG_COMMAND} : Uploads the log.


join this group for help -- @torrentleechgdrivesupport
And also don't forget to fork this repo: <a href="https://github.com/gautamajay52/TorrentLeech-Gdrive">TorrentLeech-Gdrive</a>
'''
    await message.reply_text(help_msg, disable_web_page_preview=True)


async def rename_message_f(client, message):
    inline_keyboard = []
    inline_keyboard.append([
        pyrogram.InlineKeyboardButton(
            text="read this?",
            url="https://t.me/keralagram/698909"
        )
    ])
    reply_markup = pyrogram.InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "please use @renamebot",
        quote=True,
        reply_markup=reply_markup
    )
