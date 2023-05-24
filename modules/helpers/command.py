from typing import Union, List
from pyrogram import filters

other_filters = filters.group 
other_filters2 = filters.private 


def commandpro(commands: Union[str, List[str]]):
    return filters.command(commands,"")
