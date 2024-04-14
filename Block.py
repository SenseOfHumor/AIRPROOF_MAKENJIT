import hashlib

class Block:
    def __init__(self, previous_hash, transactions):
        self.transactions = transactions
        self.previous_hash = previous_hash
        # self.time = time
        string_to_hash = "".join(transactions) + previous_hash  # concatenate transactions and previous hash
        # Encode the string before hashing
        string_to_hash_encoded = string_to_hash.encode()
        self.block_hash = hashlib.sha256(string_to_hash_encoded).hexdigest()  # hexdigest() to get a string representation of the hash