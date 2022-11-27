class Stack:
  # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
  def __init__(self):
    self.total = 0
    self.stack = []

  def push(self, data):
    # write your code to add data following LIFO and return the Stack
    self.stack.insert(0, data)
    self.total += 1
    return self.stack

  def pop(self):
    # write your code to removes the data following LIFO and return the Stack
    self.stack.remove(self.stack[0])
    self.total -= 1
    return self.stack

  def size(self):
    # write your code that returns the size of the Stack
    return self.total
  
s1 = Stack() #initialize s1 
s1.push('first in') #add this string to the stack, and continue
s1.push('second in')
s1.push('third in')
print(s1.stack) #-> ['third in', 'second in', 'first in']
s1.pop() #remove last added item ('third in')
print(s1.stack) #-> ['second in', 'first in']
