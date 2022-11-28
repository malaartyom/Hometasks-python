class LRUCache:
    def __init__(self, capicity):
        self.cap = capicity
        self.data = dict()
        self.len = 0
        self.call = dict()
    
    def put(self, key, value):
        if self.len < self.cap:
            self.data[key] = value
            self.call[key] = 0
        else:
            key_to_del = min(self.call, key=lambda x: self.call[x])

    def get(self, key):
        if (key, self.data[key]) in self.data.items():
            self.call[key] += 1
            return self.data[key]
        else:
            return None