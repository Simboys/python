class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class singly:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        node=Node(data)
        if self.tail:
            self.tail.next=node
            self.tail=node
        else:
            self.head=node
            self.tail=node
    def print(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next
ob=singly()
ob.append("java")
ob.append("python")
ob.append("c")
ob.print()
