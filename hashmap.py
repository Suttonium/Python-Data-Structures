class HashMap:
    def __init__(self):
        self.hashmap = [[] for i in range(256)]

    def __str__(self):
        pass

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hashmap)
        key_exists = False
        bucket = self.hashmap[hash_key]
        i = None
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def retrieve(self, key):
        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            return v
        raise KeyError
