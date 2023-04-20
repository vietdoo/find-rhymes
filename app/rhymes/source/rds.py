"""
import MySQLdb

from source.utils import clean_string
from source.varient import *

def sql_count(text):
    cur.execute(text)
    db.commit()
    return cur.fetchone()[0]

def sql(text):
    cur.execute(text)
    db.commit()
    return cur.rowcount


def create_sql_from_list(word_list):
    pass_dup = ' As new on DUPLICATE KEY UPDATE TV = new.TV'
    words_split = '"),("'.join(word_list)[:-3]
    return 'INSERT IGNORE INTO full_original VALUE("' + words_split


def insert_words_to_SQL(word_list):
    sql(create_sql_from_list(word_list))

def insert_word_to_SQL(word_text):
    word_text = clean_string(word_text)
    return sql('INSERT IGNORE INTO full_original VALUE("' + word_text + '")')

"""