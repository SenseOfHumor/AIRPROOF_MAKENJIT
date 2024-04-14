from Block import Block

blockchain = []

"genesis block is first block.....used to call the blockchain"
"give blockchain a previous hash,...and then array of transactions"

# genesis_block = Block("Chancellor on the brink.....", ["Maria sent 5 BTC to Jenny","Satoshi sent 10 BTC to Ivan"])

# second_block = Block(genesis_block.block_hash, ["Ivan sent 5 BTC to Liz"])

# print("Block hash: Genesis Block")
# print(genesis_block.block_hash)

# print("Block hash: Second Block")
# print(second_block.block_hash)

## using for loop to create multiple blocks in the blockchain
howMany = int(input("how many blocks you want to create: "))

for i in range(howMany):
    transactions = input("Enter transactions: ")
    if i == 0:
        # Create genesis block with user input
        genesis_block = Block("Initial hash", transactions)
        blockchain.append(genesis_block)
    else:
        # Create other blocks with user input
        block = Block(blockchain[i-1].block_hash, transactions)
        blockchain.append(block)

for block in blockchain:
    print("Block hash: ", block.block_hash)
    print("Previous hash: ", block.previous_hash)
    print("Transactions: ", block.transactions)
    print("\n")
