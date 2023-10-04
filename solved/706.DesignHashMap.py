class MyHashMap:

  def __init__(self):
    self.keys = []
    self.vals = []

  def put(self, key, value):
    if key in self.keys:
      self.vals[self.keys.index(key)] = value
    else:
      self.keys.append(key)
      self.vals.append(value)
        
  def get(self, key):
    if key in self.keys:
      return self.vals[self.keys.index(key)]
    else:
      return -1

  def remove(self, key):
    if key in self.keys:
      i = self.keys.index(key)
      self.keys = self.keys[:i] + self.keys[i+1:]
      self.vals = self.vals[:i] + self.vals[i+1:]

s = MyHashMap()
s.put(2,22)
print(s.get(2))
s.put(4,44)
s.put(2,222)
print(s.get(4))
s.remove(2)
print(s.get(2))
