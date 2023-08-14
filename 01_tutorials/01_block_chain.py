import hashlib

class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf8'))
        return sha.hexdigest()
    
class Blobkchain:
    def __init__(self):
        self.chain = [self.generic_block()]

    def generic_block(self):
        return Block("Generic block","0")
    
    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(data, prev_block.hash)
        self.chain.append(new_block)

bc = Blobkchain()
bc.add_block("My first block")