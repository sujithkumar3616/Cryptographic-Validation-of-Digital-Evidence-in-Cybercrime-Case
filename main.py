import os
from modules.hashing import generate_hash
from modules.store_hash import store_hash
from modules.verify import verify_file
from modules.report import generate_report

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "extracted_evidence", "chat_log.txt")
file_name = os.path.basename(file_path)

hash_value = generate_hash(file_path)
print("SHA-256 Hash:", hash_value)

#store_hash(file_name, hash_value)

# Get verification result
status = verify_file(file_path)

if status == "AUTHENTIC":
    print("Evidence is AUTHENTIC")
elif status == "TAMPERED":
    print("Evidence is TAMPERED")
else:
    print(status)

# Generate report with correct status
generate_report(file_name, hash_value, status)