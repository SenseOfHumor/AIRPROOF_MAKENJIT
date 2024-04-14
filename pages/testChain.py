import hashlib


class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = str(self.data) + str(self.previous_hash)
        return hashlib.sha256(data_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(data, previous_block.hash)
        self.chain.append(new_block)


# Simulate blockchain
blockchain = Blockchain()
blockchain.add_block("Test String 1")
blockchain.add_block("Test String 2")

# Retrieve data and verify immutability
latest_block = blockchain.get_latest_block()
print(f"Latest Data: {latest_block.data}")

# Attempt to tamper with data (will result in different hash)
blockchain.chain[1].data = "Tampered Data"

# Verify immutability by checking hash
if latest_block.hash != blockchain.get_latest_block().hash:
    print("Blockchain tampered with!")
else:
    print("Blockchain remains immutable.")
