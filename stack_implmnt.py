class Stack:
    def __init__(self):
        self.stack=[]
    def add(self,dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]
    def remove(self):
        if len(self.stack)<=0:
            return("No elements in the stack")
        else:
            return self.stack.pop()
    def printlist(self):
        print(self.stack)
obj=Stack()
obj.add("56")
obj.add("78")
obj.add(23)
print("Before removing stack:")
obj.printlist()
print("Peek value:",obj.peek())
print("After removing element in stack:")
obj.remove()
obj.printlist()

