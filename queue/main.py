class Queue:
  def __init__ (self,cap = 5) :
    self._a = [None for _ in range(cap)]
    self._front = 0
    self._rear = -1
    self._c = 0
  def peek(self):
    if self._c == 0 :
      return "No Elements"
    return self._a[self._front]
  def enqueue(self,data):
    self.a[self._c] = data

queue = Queue()
queue.enqueue(10)
print(queue.peek())