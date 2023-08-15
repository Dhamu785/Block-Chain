import hashlib
class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = hashlib.sha256()
        self.nonce = 0

    def mine_b(self, difficulty):
        print("Block mining - In progress....")
        self.hash.update(str(self).encode('utf8'))
        while int(self.hash.hexdigest(), 16) > 2**(256-difficulty):
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf8'))

    def __str__(self):
        return f"{self.previous_hash.hexdigest()}{self.nonce}{self.data}"
        # return f"{self.previous_hash}{self.nonce}{self.data}"
