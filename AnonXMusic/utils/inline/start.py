from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="💘 𝗞𝗜𝗗𝗡𝗔𝗣 𝗠𝗘 💘", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="✴️ 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 ✴️", url=f"https://t.me/Trending_Era"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="☯️ 𝗞𝗜𝗗𝗡𝗔𝗣 𝗠𝗘 ☯️",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="⚜️ 𝗢𝗪𝗡𝗘𝗥 ⚜️", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="🔰 𝗔𝗡𝗬 𝗤𝗨𝗘𝗥𝗬 ❓🔰", url=f"https://t.me/Abhi_rss"),
        ],
        
    ]
    return buttons
