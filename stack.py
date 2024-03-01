class Stack:
  def __init__(self, limit):
    self.stack = [None for i in range(limit)]
    self.top = -1
    self.limit = limit
    
  def isFull(self):
    if self.top + 1 == self.limit:
      return True
    return False
  
  def isEmpty(self):
    if self.top == -1:
      return True
    return False
    
  def push(self, item):
    if not self.isFull():
      self.top += 1
      self.stack[self.top] = item
    else: print("Stack full")
  
  def pop(self):
    if not self.isEmpty():
      item = self.stack[self.top]
      self.stack[self.top] = None
      self.top -= 1
      return item
    else: print("Stack empty")
    
  def peek(self):
    return self.stack[self.top]

  def display(self):
    print("----------")
    for i in range(len(self.stack)):
      print(f"| {self.stack[len(self.stack) - i - 1]} |")
    print("----------")
    
  def reverse(self):
    temp = []
    for i in range(self.top + 1):
      temp.append(self.stack[i])

    for i, x in enumerate(temp[::-1]):
      self.stack[i] = x