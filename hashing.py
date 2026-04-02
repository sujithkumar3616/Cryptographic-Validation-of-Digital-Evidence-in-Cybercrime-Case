import hashlib

def generate_hash(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(block)

    return sha256_hash.hexdigest()