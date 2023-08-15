import hashlib
from block import Block

class Chain:
    def __init__(self, difficulity):
        self.difficulity = difficulity
        self.blocks = []
        self.pool = []
        self.generic_block()

    def proof_of_work(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf8'))
        return hash.hexdigest() == block.hash.hexdigest() and int(hash.hexdigest(), 16) < 2**(256-self.difficulity) and block.previous_hash == self.blocks[-1].hash
    
    def add_block(self, block):
        if self.proof_of_work(block):
            self.blocks.append(block)
        else:
            print("Failed to add block")

    def add_pool(self, data):
        self.pool.append(data)

    def mine(self):
        if len(self.pool) > 0:
            block = Block(self.pool.pop(), self.blocks[-1].hash)
            block.mine_b(self.difficulity)
            self.add_block(block)
        else:
            print("less than 0")

    def generic_block(self):
        h = hashlib.sha256()
        h.update(''.encode('utf8'))
        origin = Block("Origin",h)
        origin.mine_b(self.difficulity)
        self.blocks.append(origin)
        print("Generic block created...")