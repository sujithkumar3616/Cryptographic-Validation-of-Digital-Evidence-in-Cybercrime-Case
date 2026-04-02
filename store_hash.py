import sqlite3

def store_hash(file_name, hash_value):

    conn = sqlite3.connect("database/evidence.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evidence_hash(
        file_name TEXT PRIMARY KEY,
        hash_value TEXT
    )
    """)

    cursor.execute("""
    INSERT OR REPLACE INTO evidence_hash(file_name, hash_value)
    VALUES (?, ?)
    """, (file_name, hash_value))

    conn.commit()
    conn.close()

    print("Hash stored successfully.")