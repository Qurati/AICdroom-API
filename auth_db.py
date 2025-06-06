import psycopg2
from typing import Optional
from config import *

def connect():
    connection = psycopg2.connect(user=user_db,
                                  password=password_db,
                                  host=host_db,
                                  port="5432",
                                  database=database_db)
    conn = connection
    return conn

# Функция для получения курсора
def get_cursor():
    conn = connect()
    return conn, conn.cursor()

def init_db():
    conn, cursor = get_cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS auth_tokens (
                token TEXT PRIMARY KEY,
                code TEXT,
                verified INTEGER DEFAULT 0,
                telegram_user_id INTEGER
            )
        """)
    conn.commit()


def create_token(token: str):
    conn, cursor = get_cursor()
    cursor.execute("INSERT INTO auth_tokens (token) VALUES (%s)", (token,))
    conn.commit()



def get_token_by_code(code: str) -> Optional[dict]:
    conn, cursor = get_cursor()
    cursor.execute("""
            SELECT token, telegram_user_id, verified FROM auth_tokens
            WHERE code = %s
        """, (code,))
    row = cursor.fetchone()
    if row:
        return {"token": row[0], "telegram_user_id": row[1], "verified": bool(row[2])}
    return None