from dataclasses import dataclass
from typing import List

from aiogram.types import LabeledPrice

from data import config


@dataclass
class Item():
    title: str
    description: str
    currency: str
    prices: List["LabeledPrice"]
    start_parameter: str
    provider_data: dict = None
    photo_url: str = None
    photo_size: int = None
    photo_width: int = None
    photo_height: int = None
    need_name: bool = False
    need_phone_number: bool = False
    need_email: bool = False
    need_shipping_address: bool = False
    send_phone_number_to_provider: bool = False
    send_email_to_provider: bool = False
    is_flexible: bool = False

    provider_token: str = config.PROVIDER_TOKEN

    def generete_invoice(self):
        return self.__dict__
