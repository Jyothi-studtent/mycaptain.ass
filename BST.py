class BT:
    def __init__(self,data):
        self.lchild=None
        self.data=data
        self.rchild=None
    
    def insert(self,key):
        if key > self.data:
            if self.rchild is None:
                self.rchild=BT(key)
            else:
                self.rchild.insert(key)
        elif key < self.data:
            if self.lchild is None:
                self.lchild=BT(key)
            else:
                self.lchild.insert(key)
                
    
    def pre(self):
        if self :
            print(self.data)
            if self.lchild is not None:
                self.lchild.pre()
            if self.rchild is not None:
                self.rchild.pre()
                
    def inord(self):
        if self.lchild is not None:
            self.lchild.inord()
        print(self.data)    
        if self.rchild is not None:
            self.rchild.inord()
                
    def postord(self):
        if self.lchild is not None:
            self.lchild.postord()
        if self.rchild is not None:
            self.rchild.postord()
        print(self.data)
    def nodes(self):
        if self.lchild is None:
            x=0
        else:
            x=self.lchild.nodes()
        if self.rchild is None:
            y=0
        else:
            y=self.rchild.nodes()
        return 1+x+y 
        
        
    def leafnodes(self):
        if self.lchild is None:
            x=0
        else:
            x=self.lchild.leafnodes()
        if self.rchild is None:
            y=0
        else:
            y=self.rchild.leafnodes()
        if self.lchild is None and self.rchild is None:
            return x+y+1
        else:
            return x+y
    def degreeof2(self):
        if self.lchild is None:
            x=0
        else:
            x=self.lchild.degreeof2()
        if self.rchild is None:
            y=0
        else:
            y=self.rchild.degreeof2()
        if self.lchild and self.rchild:
            return 1+x+y
        else:
            return x+y
        
        
        
        
        
        
        
        
    def height(self):
        if self.lchild is None:
            x=0
        else:
            x=self.lchild.height()
        if self.rchild is None:
            y=0
        else:
            y=self.rchild.height()
        return 1+max(x,y)
        
    def search(self,key):
        if self.data==key:
            return self
        if key >self.data:
            if self.rchild is None:
                return None
            else:
                return self.rchild.search(key)
        elif key<self.data:
            if self.lchild is None:
                return None
            else:
                return self.lchild.search(key)
                
                
t1=BT(30)

t1.insert(20)
t1.insert(40)
t1.insert(30)
t1.insert(20)
t1.inord()




