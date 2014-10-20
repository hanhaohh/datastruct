class LinkeQueue:
    class _Node:
        def __init__(self,value,next_ele=None):
            self._value = value
            self._next = next_ele
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.size==0
    def enqueue(self,element):
        node = self._Node(element)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail._next = node
        self.tail = node
        self.size+=1
    def first(self):
        if self.is_empty():
            raise Exception("stoo")
        else:
            return self.head._value
    def dequeue(self):
        if self.size==0:
            raise Exception("stop")
        answer = self.head._value
        self.head = self.head._next 
        self.size= self.size -1
        if self.is_empty():
            self.tail = None
        return answer
        
    
