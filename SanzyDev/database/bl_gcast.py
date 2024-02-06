# Ayiin - Userbot
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

from .core import db

conn = db.get_conn()


# ========================×========================
#              BLACKLIST GCAST DATABASE
# ========================×========================

def cek_gcast(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    cursor = conn.execute(
        "SELECT bl_gcast FROM blacklist_gcast WHERE user_id = ?", (user_id,)
    )
    try:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    except:
        return []


def add_gcast(user_id: int, chat_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    x = cek_gcast(user_id)
    if x:
        xx = eval(x)
        xx.append(chat_id)
        conn.execute("""UPDATE blacklist_gcast SET bl_gcast = ? WHERE user_id = ?""", (str(xx), user_id))
    else:
        x.append(chat_id)
        conn.execute("""INSERT INTO blacklist_gcast (user_id, bl_gcast) VALUES(?,?)""", (user_id, str(x)))
    conn.commit()


def del_gcast(user_id: int, chat_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    x = eval(cek_gcast(user_id))
    x.remove(chat_id)
    conn.execute("""UPDATE blacklist_gcast SET bl_gcast = ? WHERE user_id = ?""", (str(x), user_id))
    conn.commit()
