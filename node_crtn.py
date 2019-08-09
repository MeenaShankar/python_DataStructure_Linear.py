class Node:
    def __init__(self,x):
        self.data=x
        self.adrs=None
n1=Node(500)
n2=Node(400)
n3=Node(200)
n4=Node(100)
n5=Node(300)
n4.adrs=n3
n3.adrs=n5
n5.adrs=n2
n2.adrs=n1
temp=n4
while temp:
    print(temp.data,"-->",end="")
    temp=temp.adrs
    if(temp==None):
        print("None")
        break
