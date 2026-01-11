# Calls Music 1 - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Roj Serbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

from typing import Union, List
from pyrogram import filters
from config import COMMAND_PREFIXES

# Humne yahan se ~filters.edited hata diya hai taaki crash na ho
other_filters = filters.group & ~filters.via_bot & ~filters.forwarded
other_filters2 = filters.private & ~filters.via_bot & ~filters.forwarded

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
