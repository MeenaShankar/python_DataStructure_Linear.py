class Node:
    def __init__(self,data):
        self.data=data
        self.nxt=None
class SSL:
    def __init__(self):
       self.head=None
    def InsertAtBeg(self,data):
        temp=Node(data)
        temp.nxt=self.head
        self.head=temp
    def DelAtBeg(self):
        temp=self.head
        self.head=self.head.nxt
        temp=None
    def PrintList(self):
        temp=self.head
        while temp:
            print(temp.data,"==>",end="")
            temp=temp.nxt
        print("None")
            
        
obj=SSL()
ch=0
while(ch!=4):
    print("1.Insert 2.Delete  3.Print  4.Exit")
    ch=int(input("Enter ur choice:"))
    if(ch==1):
        a=input()
        obj.InsertAtBeg(a)
        obj.PrintList()
    elif(ch==2):
        obj.DelAtBeg()
        obj.PrintList()
    elif(ch==3):
        obj.PrintList()
    else:
        break
