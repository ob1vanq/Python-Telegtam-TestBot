from aiogram import Dispatcher

from .privat_chat import IsPrivate
from.admin_filter import AdminFilter
from .group_chat import IsGroup
from .forward_message import IsForwarded


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsGroup)

