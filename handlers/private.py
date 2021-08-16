from time import time
from datetime import datetime
from helpers.filters import command, sudo_only
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>┗┓ Hi {message.from_user.first_name} My Name is [ɪꜰᴀᴀ ᴍᴜꜱɪᴄ](https://t.me/Ifaamusic_Bot) ┏┛\n
I'm Bot Music Group, Which Can Play Songs in Group Voice Chat In Easy Way
I Have Many Practical Features Like:
┏━━━━━━━━━━━━━━
┣• Play music.
┣• Download Songs.
┣• Search for the song you want to play or download.
┗━━━━━━━━━━━━━━
Type » /help « To View List of Commands!
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan Ke Group ➕", url=f"https://t.me/Ifaamusic_Bot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                         "🤖 Assistant", url=f"https://t.me/Niifaya"
                    ),
                    InlineKeyboardButton(
                        "🛠 Repo", url="https://github.com/UserLazy/LazyMusicbot"
                    )
                ]
            ]
        ),
     disable_web_page_preview=False
    )


@Client.on_message(command(["start", f"start@Ifaamusic_Bot"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""I'm online!\n<b>Up since:</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Repo", url="https://github.com/UserLazy/LazyMusicbot"
                    ),
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/OdaSupport"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.mention()}!
\n/play (song title/link/audio) — To Play the song you requested via YouTube
/song (song title) - To Download songs from YouTube
/search (video title) — To Search Videos on YouTube with details
\n**Admins Only:**
/pause - To Pause Song playback
/resume - To resume playback of the paused song
/skip - To Skip playback of the song to the next Song
/end - To Stop Song playback
/userbotjoin - To Invite assistant to your chat
/reload - To refresh admin list
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group", url="https://t.me/OdaSupport"
                    ),
                    InlineKeyboardButton(
                        "Oda", url="https://t.me/OdaRobot"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@Ifaamusic_Bot"]) & ~filters.edited)
async def ping_pong(client: Client, m: Message):
    start = time()
    m_reply = await m.reply_text("Pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        f"🏓 **PONG!!**\n"
        f"`{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@Ifaamusic_Bot"]) & sudo_only & ~filters.edited)
async def get_uptime(client: Client, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        f"🤖\n"
        f"• **Uptime:** `{uptime}`\n"
        f"• **Start Time:** `{START_TIME_ISO}`"
    )
