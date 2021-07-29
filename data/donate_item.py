from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.item import Item

Cookie = Item(
    title="Донат",
    description="В поддержку разработчика бота",
    currency="UAH",
    prices= [
        LabeledPrice(
            label="Донат",
            amount=10_00
        )

    ],
    start_parameter="create_donate",
    photo_url="https://s3.amazonaws.com/imagesroot.rescuegroups.org/webpages/s8263nhgnuqgs8jc.png",
    photo_width=250,
    photo_height=250,
    need_name=True,
    need_shipping_address=False,
    is_flexible=True
)

DONATE = types.ShippingOption(
    id="DONATE",
    title="Комиссия",
    prices=[
            LabeledPrice(
                 label="Комиссия",
                 amount= 0
        )
    ]
)
