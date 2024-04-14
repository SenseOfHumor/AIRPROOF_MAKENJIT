from Block import Block

blockchain = []

"genesis block is first block.....used to call the blockchain"
"give blockchain a previous hash,...and then array of transactions"

genesis_block = Block("Chancellor on the brink.....", ["Maria sent 5 BTC to Jenny"])

second_block = Block(genesis_block.block_hash, ["Ivan sent 5 BTC to Liz"])

print("Block hash: Genesis Block")
print(genesis_block.block_hash)

print("Block hash: Second Block")
print(second_block.block_hash)