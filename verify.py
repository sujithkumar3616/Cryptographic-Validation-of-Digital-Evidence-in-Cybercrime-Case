import sqlite3
from modules.hashing import generate_hash
import os

def verify_file(file_path):

    conn = sqlite3.connect("database/evidence.db")
    cursor = conn.cursor()

    file_name = os.path.basename(file_path)

    cursor.execute(
        "SELECT hash_value FROM evidence_hash WHERE file_name=?",
        (file_name,)
    )

    result = cursor.fetchone()

    if result is None:
        conn.close()
        return "No stored hash found"

    stored_hash = result[0]
    new_hash = generate_hash(file_path)

    if stored_hash == new_hash:
        conn.close()
        return "AUTHENTIC"
    else:
        conn.close()
        return "TAMPERED"