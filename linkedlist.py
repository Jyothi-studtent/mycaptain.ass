class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        
    def nodesnum(self):
        a=self.head
        count=0
        while a is not None:
            a=a.next
            count+=1
        return count    
        
    def sumofnode(self):
        sum=0
        a=self.head
        while a is not None:
            sum+=a.data
            a=a.next
        return sum
        
    def maxi(self):
        a=self.head
        ans=a.data
        while a is not None:
            if a.data > ans:
                ans=a.data
            a=a.next    
        return ans
        
    def display(self):
        
        a=self.head
        
        while a is not None:
            print(a.data)
            a=a.next
        
n1=node(2)
n2=node(4)
n3=node(6)
n4=node(8)
n5=node(10)
sll=Linkedlist()
sll.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
print(sll.maxi())
print(sll.nodesnum())
print(sll.sumofnode())
print()
sll.display()
    
        
