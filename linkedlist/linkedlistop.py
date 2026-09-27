class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class linkedlist:
  def __init__(self):
    self.head=None
    self.size = 0
  def append(self,data):
    if self.head==None:
      self.head=Node(data)
      self.size += 1
      return
    cn=self.head
    while cn.next is not None:
      cn=cn.next
    cn.next=Node(data)
    self.size += 1
  def traversal(self):
    cn=self.head
    while cn.next is not None:
      print(cn.data,end="->")
      cn=cn.next
    print(cn.data,end="->")
    print(cn.next)
  def search(self,data):
    if self.head is None :
      print("no elements in the ll")
      return
    cn = self.head
    ind = 0
    while cn.next is not None :
      if cn.data == data :
        print(f"element {data} is found at {ind} index")
        return
      cn = cn.next
      ind +=1
    if cn.data == data :
      print(f"Element {data} is found at {ind} index ")
      return
    print("Element not found")
  def len(self):
    return self.size
  def insStart(self,data):
    obj=Node(data)
    obj.next=self.head
    self.head=obj
    self.size+=1
  def delstart(self):
    if self.head is None:
        return
    elif self.head.next is None:
        self.head=None
        return
    cn=self.head
    while cn.next.next is not None:
        cn=cn.next
    cn.next=None
  def insAt(self,data,pos):
    if pos < 0 or pos > self.size:
      return
    if pos == 0:
      self.insStart(data)
      return
    ind=0
    cn=self.head
    while ind + 1 < pos:
      cn=cn.next
      ind+=1
    obj=Node(data)
    obj.next=cn.next
    cn.next=obj
    self.size+=1

    

ll=linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.traversal()
ll.search(30)
print(ll.len())
ll.insStart(100)
ll.traversal()
ll.delstart()
ll.traversal()
ll.delstart()
ll.traversal()