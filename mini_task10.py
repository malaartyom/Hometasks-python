class LRUCache:
    def __init__(self, capicity):
        self.cap = capicity
        self.data = dict()
        self.len = 0
        self.call = dict()
    
    def put(self, key, value):
        if self.len < self.cap:
            if key in self.data.keys():
                self.call[key] += 1
            else:
                self.call[key] = 0
                
            self.data[key] = value
        else:
            key_to_del = min(self.call, key=lambda x: self.call[x])
            del self.data[key_to_del]

    def get(self, key):
        if (key, self.data[key]) in self.data.items():
            self.call[key] += 1
            return self.data[key]
        else:
            return None