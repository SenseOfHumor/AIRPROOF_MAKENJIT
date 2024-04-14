import hashlib
from flask import Flask, request
import jsonify
import requests


app = Flask(__name__)

class Block:
    def __init__(self, previoushash, transactions):
        self.transactions = transactions
        self.previoushash = previoushash
        #self.time = time
        stringtohash = "".join(transactions) + previoushash  # concatenate transactions and previous hash
        # Encode the string before hashing
        string_to_hash_encoded = stringtohash.encode()
        self.block_hash = hashlib.sha256(string_to_hash_encoded).hexdigest()  # hexdigest() to get a string representation of the hash

blockchain = []

@app.route('/blocks', methods=['GET'])
def get_blocks():
    return jsonify(blockchain)

@app.route('/blocks', methods=['POST'])
def add_block():
    data = request.get_json()
    if 'previous_hash' not in data or 'transactions' not in data or 'time' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    new_block = Block(data['previous_hash'], data['transactions'], data['time'])
    blockchain.append(new_block.__dict)
    return jsonify({'message': 'Block added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)
