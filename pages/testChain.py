import hashlib


def create_blockchain(data):
  """Creates a blockchain with a genesis block and a block containing the data"""
  # Define block structure (similar to class attributes)
  def Block(data, previous_hash):
    block = {
        "data": data,
        "previous_hash": previous_hash,
        "hash": calculate_hash(data, previous_hash)
    }
    return block

  def calculate_hash(data, previous_hash):
    data_string = str(data) + str(previous_hash)
    return hashlib.sha256(data_string.encode()).hexdigest()

  # Blockchain operations (similar to class methods)
  chain = [Block("Genesis Block", "0")]

  def get_latest_block():
    return chain[-1]

  def add_block(new_data):
    previous_block = get_latest_block()
    new_block = Block(new_data, previous_block["hash"])
    chain.append(new_block)

  # Add the provided data block
  add_block(data)

  # Return the entire blockchain data structure
  return chain

# Test Cases
# blockchain1 = create_blockchain("Swap")
# print(f"Latest Block - {blockchain1[-1]['data']}")
# #printing the hash of the latest block
# print(f"Latest Block - {blockchain1[-1]['hash']}")

# blockchain2 = create_blockchain("Swapnil")
# print(f"Latest Block - {blockchain2[-1]['data']}")
# #printing the hash of the latest block
# print(f"Latest Block - {blockchain2[-1]['hash']}")
