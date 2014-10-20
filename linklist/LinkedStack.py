class LinkedStack:
    class _Node:
        def __init__(self,value,next_ele=None):
            self._value = value
            self._next = next_ele
    def __init__(self):
        self.head = self._Node(None,None)
        self.size = 0 
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def push(self,element):
        self.head = self._Node(element,self.head)
        self.size+=1
    def top(self):
        return self.head._value
    def pop(self):
        if self.size==0:
            raise Exception("stop")
        answer = self.head._value
        self.head = self.head._next 
        self.size= self.size -1
        return answer
        
    
