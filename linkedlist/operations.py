class Node:
  def __init__(self,data):
    self.data=data
    self.next=None


class linkedlist:
  def __init__(self):
    self.head=None
  def append(self,data):
    if self.head==None:
      self.head=Node(data)
      return
    cn=self.head
    while cn.next is not None:
      cn=cn.next
    cn.next=Node(data)
  def traversal(self):
    cn=self.head
    while cn.next is not None:
      print(cn.data,end="->")
      cn=cn.next
    print(cn.data,end="->")
    print(cn.next)
  def search(self,data):
    if self.head is None:
      print('no element in the LL')
      return
    cn=self.head
    ind=0
    while cn.next is not None:
      if cn.data==data:
        print(f'element(data)is found at {ind} index')
        return
      cn=cn.next
      ind+=1
    if cn.data==data:
      print(f'element {data} is found at {ind} index')
      return
    print('Element not found')
ll=linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.traversal()
ll.search(50)