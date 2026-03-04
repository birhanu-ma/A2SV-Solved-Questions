class RandomizedSet:

    def __init__(self):
        self.value = []
        self.valuesIdx = {}

    def insert(self, val: int) -> bool:
        if val in self.valuesIdx:
            return False
        self.valuesIdx[val] = len(self.value)
        self.value.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valuesIdx:
            return False
        index = self.valuesIdx[val]
        self.valuesIdx[self.value[-1]] = index
        del self.valuesIdx[val]
        self.value[index] = self.value[-1]
        self.value.pop()
        return True
        
        

    def getRandom(self) -> int:
        index = random.randint(0, len(self.value) - 1)
        return self.value[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
