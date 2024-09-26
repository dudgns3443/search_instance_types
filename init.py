import sqlite3

# mydatabase.db 파일 생성 및 SQLite 연결
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# 테이블 생성 (예: 검색 기록 저장 테이블)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS search_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        instance_type TEXT NOT NULL,
        region TEXT NOT NULL,
        price REAL NOT NULL,
        search_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# 커밋 및 연결 종료
conn.commit()
conn.close()