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

from .core import db

conn = db.get_conn()


# ========================×========================
#              BLACKLIST GCAST DATABASE
# ========================×========================

def sudoer():
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    cursor = conn.execute(
        "SELECT user_id FROM sudoer"
    )
    try:
        row = cursor.fetchone()
        cursor.close()
        return row[0]
    except:
        return []


def add_sudo(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    x = sudoer()
    if x:
        xx = eval(x)
        xx.append(user_id)
        conn.execute("""UPDATE sudoer SET user_id = ?""", (str(xx), user_id))
    else:
        x.append(user_id)
        conn.execute("""INSERT INTO sudoer (user_id) VALUES(?)""", (str(x),))
    conn.commit()


def del_sudo(user_id: int):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    x = eval(sudoer())
    x.remove(user_id)
    conn.execute("""UPDATE sudoer SET user_id = ?""", (str(x),))
    conn.commit()
