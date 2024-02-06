# Sanzy - Userbot
# Copyright (C) 2022-2023 @sanzydevv
#
# This file is a part of < https://github.com/sanzydev/Sanzy-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/sanzydev/Sanzy-Userbot/blob/main/LICENSE/>.
#
# FROM Sanzy-Userbot <https://github.com/sanzydev/Sanzy-Userbot>
# t.me/SanzyChats & t.me/Sanzy_updatebot


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import os
import sys

from SanzyDev import CMD_HELP
from SanzyDev.sanzy import sanzy_cmd, runcmd

from . import cmd


@sanzy_cmd(pattern="getdb")
async def db_backup(e):
    if os.path.exists('sanzy.db'):
        await e.client.send_file(
            entity=e.chat_id,
            file='sanzy.db',
            thumb="SanzyDev/resources/logo.jpg",
            caption=f'Database {(await e.client.get_me()).first_name}',
            force_document=True,
        )
        return
    else:
        await e.edit("Maaf database tidak ditemukan.")
        return


@sanzy_cmd(pattern="setdb")
async def db_backup(e):
    xx = await e.reply("**Memproses...**")
    path = os.getcwd()
    reply = await e.get_reply_message()
    if 'sanzy.db' in os.listdir():
        await xx.edit("**Database `sanzy.db` ditemukan. Menghapus `sanzy.db` Dari Directory.**")
        os.remove('sanzy.db')
    media = reply.media
    if hasattr(media, "document"):
        file_doc = await reply.download_media()
        os.path.join(path, file_doc)
        await runcmd(f"cp {path}/{file_doc} {path}/sanzy.db")
        await xx.delete()
        await e.reply("**Database Berhasil digunakan. Sedang merestart userbot**")
        args = [sys.executable, "-m", "SanzyDev"]
        os.execle(sys.executable, *args, os.environ)


CMD_HELP.update(
    {
        "database": f"**Plugin : **`database`\
        \n\n  »  **Perintah :** `{cmd}getdb`\
        \n  »  **Kegunaan : **Untuk mengambil database anda.\
        \n\n  »  **Perintah :** `{cmd}setdb [reply document]`\
        \n  »  **Kegunaan : ** Balas ke Pesan Document untuk mengatur database anda yang sebelumnya telah anda ambil.\
        \n\n **CATATAN :** Simpan database anda dengan baik agar anda dapat menggunakannya kembali dengan perintah `{cmd}setdb`\
    "
    }
)
