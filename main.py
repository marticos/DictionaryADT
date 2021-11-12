### Dictionary ADT
### Implementation hash table implementation

### Count repetitionsx

class DictionaryADT:
  def __init__(self):
    self.table = [None] * 10

  def insert(self, key):
    index = self.hash_func(key)
    node = self.table[index]
    while node:
      if node.key == key:
        node.value += 1
      node = node.next
    node = Node(key, 1)

  def hash_func(self, key):
    return key % 10

  def look_up(self, key):
    index = self.hash_func(key)
    node = self.table[index]
    while node:
      if node.key == key:
        return node
      node = node.next
    return None
  
  def delete(self, key):


class Node:
  def __init__(self, key = None, value = None, next = None):
    self.key = key
    self.value = value
    self.next = next

### WORK IN PROGRESS