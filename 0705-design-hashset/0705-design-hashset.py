class MyHashSet:

    def __init__(self):
        self.sett = set()

    def add(self, key: int) -> None:
        self.sett.add(key)
        return self.sett

    def remove(self, key: int) -> None:
        if key in self.sett:
            self.sett.remove(key)
        else:
            return self.sett
        

    def contains(self, key: int) -> bool:
        return True if key in self.sett else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)