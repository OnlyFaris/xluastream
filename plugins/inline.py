"""
xluastream, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/OnlyFaris>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

from config import Config
from helpers.log import LOGGER
from pyrogram import Client, errors
from youtubesearchpython import VideosSearch
from pyrogram.handlers import InlineQueryHandler
from pyrogram.types import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup

buttons = [
            [
                InlineKeyboardButton("❔ HOW TO USE ME ❔", callback_data="help"),
            ],
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/OnlyFaris"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/AsmSupport"),
            ],
            [
                InlineKeyboardButton("🤖 MAKE YOUR OWN BOT 🤖", url="https://heroku.com/deploy?template=https://github.com/OnlyFaris/xluastream/tree/alpha"),
            ]
         ]

def get_cmd(dur):
    if dur:
        return "/play"
    else:
        return "/stream"

@Client.on_inline_query()
async def search(client, query):
    answers = []
    if query.query == "SAF_ONE":
        answers.append(
            InlineQueryResultPhoto(
                title="Deploy Own Video Player Bot",
                thumb_url="https://telegra.ph//file/3ed5eafa4a95960d33980.jpg",
                photo_url="https://telegra.ph//file/3ed5eafa4a95960d33980.jpg",
                caption=f"{Config.REPLY_MESSAGE}\n\n<b>© Powered By : \n@OnlyFaris | @AsmSupport 👑</b>",
                reply_markup=InlineKeyboardMarkup(buttons)
                )
            )
        await query.answer(results=answers, cache_time=0)
        return
    string = query.query.lower().strip().rstrip()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text=("✍️ Type An Video Name !"),
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(string.lower(), limit=50)
        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=("Duration: {} Views: {}").format(
                        v["duration"],
                        v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "{} https://www.youtube.com/watch?v={}".format(get_cmd(v["duration"]), v["id"])
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )
        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text=("❌ No Results Found !"),
                switch_pm_parameter="",
            )


__handlers__ = [
    [
        InlineQueryHandler(
            search
        )
    ]
]
