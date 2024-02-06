from .core import db

con = db.get_conn()


# ========================×========================
#              BLACKLIST FILTER DATABASE
# ========================×========================
def get_chat_blacklist(chat_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    cursor = con.execute(
        '''
        SELECT * FROM blacklist_filter WHERE chat_id = ?
        ''', (chat_id,)
    )
    try:
        ok = cursor.fetchall()
        cursor.close()
        return ok
    except:
        return None


def add_to_blacklist(chat_id, chat_title, trigger):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    con.execute(
        '''
        INSERT INTO blacklist_filter (
            chat_id,
            chat_title,
            trigger
        )
        VALUES (?, ?, ?)
        ''',
        (chat_id, chat_title, trigger)
    )
    con.commit()


def update_to_blacklist(chat_id, chat_title, trigger):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    con.execute(
        '''
        UPDATE blacklist_filter SET chat_title = ?, trigger = ? WHERE chat_id = ?
        ''',
        (chat_id, chat_title, trigger)
    )
    con.commit()


def rm_from_blacklist(chat_id, trigger):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    con.execute(
        '''
        DELETE FROM blacklist_filter WHERE chat_id = ? AND trigger = ?
        ''',
        (chat_id, trigger)
    )
    con.commit()
