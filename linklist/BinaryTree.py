#*_*coding:utf-8*_*

import os

class Node:
    
    def __init__(self, value = None, parent = None , left = None, right = None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.depth = 0

    def insert(self, n):
        if n == None:
            return

        if self.root == None:
            self.root = n
            self.size=self.size+1
            self.depth = 1
            return None

        tmp = self.root
        tmpDepth = 1
        while True:
            tmpDepth = tmpDepth+1
            if n.value <= tmp.value:
                if tmp.left == None:
                    n.parent = tmp
                    tmp.left = n
                    self.size = self.size+1
                    self.depth = max(self.depth, tmpDepth)
                    break
                else:
                    tmp = tmp.left
            elif n.value > tmp.value:
                if tmp.right == None:
                    n.parent = tmp
                    tmp.right = n
                    self.size = self.size+1
                    self.depth = max(self.depth, tmpDepth)
                    break
                else:
                    tmp=tmp.right

    def find(self, v):
        if v==None or self.root==None:
            print 'None'
            return
        tmp=self.root
        while True:
            if v==tmp.value:
                print 'find it ', v
                break
            elif v<tmp.value:
                if tmp.left==None:
                    print 'None'
                    break
                else:
                    tmp=tmp.left
            else:
                if tmp.right==None:
                    print 'None'
                    break
                else:
                    tmp=tmp.right
    def find_p(self,n,search):
        if n==None:
            return "empt"
        if search == n.value:
            return True
        if True == self.find_p(n.left, search):
            return True
        if True == self.find_p(n.right, search):
            return True

        return False
t = Tree()
for i in (6,3,4,7,8,3,2,2,5):
    t.insert(Node(i))
t.find_p(t.root,2)
