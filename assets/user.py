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
from pyrogram import Client
from pytgcalls import PyTgCalls
from helpers.log import LOGGER

USER = Client(
    Config.SESSION,
    Config.API_ID,
    Config.API_HASH,
    plugins=dict(root="assets")
    )
group_call = PyTgCalls(USER, cache_duration=180)
