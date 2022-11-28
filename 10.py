class LRUCache:
    def __init__(self, capicity):
        self.cap = capicity
        self.data = dict()
        self.len = 0
    
    def put(self, key, value):
        if self.len < self.ca
            self.data[key] = value