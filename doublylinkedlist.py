class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class doublel:
    def __init__(self):
        self.head=None
        
    def fortraversal(self):
        a=self.head
        while a is not None:
            print(a.data)
            a=a.next
    def backtraversal(self):
        a=self.head
        while a.next is not None:
            a=a.next
        while a is not None:
            print(a.data)
            a=a.prev
            
    def inserts(self,data):
        new=Node(data)
        new.next=self.head
        self.head.prev=new
        self.head=new
        
    def insertatend(self,data):
        a=self.head
        while a.next is not None:
            a=a.next
        new=Node(data)
        a.next=new
        new.prev=a
    
    def insertatpos(self,pos,data):
        newnode=Node(data)
        if pos==1:
            if self.head !=None:
                newnode.next=self.head
                self.head.prev=newnode
            self.head=newnode
        else:
            a=self.head
            i=1
            while i< pos-1:
                
                a=a.next
                i+=1
                
            newnode.next=a.next
            newnode.prev=a
            if a.next!=None:
                newnode.next.prev=newnode
            a.next=newnode
    
    
    def deleteats(self):
        self.head=self.head.next
        self.head.prev.next=None
        self.head.prev=None
    def deleteatend(self):
        a=self.head
        while a.next is not None:
            a=a.next
        a.prev.next=None
        a.prev=None
    def deleteatpos(self,pos):
        a=self.head
        i=1
        
        while i!=pos:
            
            a=a.next #a will be pointing to the node which is to be deleted
            i+=1
        a.prev.next=a.next
        a.next.prev=a.prev
        a.prev=a.next=None
dll=doublel()
dll.insertatpos(1,"monk")
dll.insertatpos(2,"peace")
dll.insertatpos(3,"discipline")
dll.insertatpos(4,"focus")

dll.insertatpos(1,"think like ....")

dll.insertatpos(4,"evalute")
dll.insertatpos(7,"byeee")
dll.insertatpos(5,"observe")
dll.deleteats()
dll.deleteatend()
dll.deleteatpos(3)
dll.deleteatpos(3)
dll.fortraversal()
                
                
                
                
            
            
            


