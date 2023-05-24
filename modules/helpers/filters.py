from typing import Union, List
from pyrogram import filters
from modules.config import COMMAND_PREFIXES

other_filters = filters.group 
other_filters2 = filters.private 


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)

