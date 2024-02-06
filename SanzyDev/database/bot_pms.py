from .core import db

con = db.get_conn()


def get_user_id(message_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    cur = con.execute(
        '''
        SELECT * FROM bot_pms WHERE message_id = ?
        ''', (message_id,)
    )
    try:
        cur.fetchone()
        cur.close()
        return cur[0]
    except:
        return None


def add_user_to_db(
    user_id,
    message_id,
    first_name,
    reply_id,
    logger_id,
    result_id
):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    check = get_user_id(message_id)
    if check:
        con.execute(
            '''
            UPDATE bot_pms 
            SET message_id = ?, first_name = ?, reply_id = ?, logger_id = ?, result_id = ?
            WHERE user_id = ?
            ''',
            (message_id, first_name, reply_id, logger_id, result_id, user_id)
        )
    else:
        con.execute(
            '''
            INSERT INTO bot_pms (
                user_id,
                message_id,
                first_name,
                reply_id,
                logger_id,
                result_id
                
            )
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (user_id, message_id, first_name, reply_id, logger_id, result_id)
        )


def del_user_from_db(message_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    con.execute(
        '''
        DELETE FROM bot_pms WHERE message_id = ?
        ''', (message_id,)
    )
    con.commit()


def get_user_reply(reply_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    cur = con.execute(
        '''
        SELECT reply_id FROM bot_pms WHERE reply_id = ?
        ''', (reply_id,)
    )
    try:
        cur.fetchone()
        cur.close()
        return cur[0]
    except:
        return None


def get_user_results(result_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    cur = con.execute(
        '''
        SELECT result_id FROM bot_pms WHERE result_id = ?
        ''', (result_id,)
    )
    try:
        cur.fetchone()
        cur.close()
        return cur[0]
    except:
        return None


def get_user_logging(logger_id):
    """
    KANG COPAS GAUSAH MAIN HAPUS KONTOL
    Copyright (C) 2023-present Sanzy <https://github.com/sanzydev>
    """
    cur = con.execute(
        '''
        SELECT logger_id FROM bot_pms WHERE logger_id = ?
        ''', (logger_id,)
    )
    try:
        cur.fetchone()
        cur.close()
        return cur[0]
    except:
        return None
