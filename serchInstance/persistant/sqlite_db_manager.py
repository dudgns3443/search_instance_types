import sqlite3
import boto3

from datetime import datetime
from config.constants import Constants

s3_client = boto3.client('s3')

def upload_db_to_s3():
    s3_client.upload_file(Constants.LOCAL_DB_PATH, Constants.BUCKET_NAME, Constants.DB_FILE_NAME)

def download_db_from_s3():
    s3_client.download_file(Constants.BUCKET_NAME, Constants.DB_FILE_NAME, Constants.LOCAL_DB_PATH)


def create_table():
    """ 검색 기록 테이블 생성 """
    with sqlite3.connect(Constants.LOCAL_DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS search_history (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            instance_type TEXT,
                            region TEXT,
                            price REAL,
                            search_time TEXT
                        )''')
        conn.commit()

def save_search_history(instance_type, region, price):
    """ 검색 기록 저장 """
    create_table()  # 테이블이 없으면 생성
    with sqlite3.connect(Constants.LOCAL_DB_PATH) as conn:
        cursor = conn.cursor()
        search_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''INSERT INTO search_history (instance_type, region, price, search_time)
                          VALUES (?, ?, ?, ?)''', (instance_type, region, price, search_time))
        conn.commit()

def fetch_search_history():
    """ 검색 기록 조회 """
    create_table()  # 테이블이 없으면 생성
    with sqlite3.connect(Constants.LOCAL_DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT instance_type, region, price, search_time FROM search_history
                          ORDER BY search_time DESC''')
        results = cursor.fetchall()
    return results