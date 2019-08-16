from pythonds.basic import Queue
def hotline(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size()>1:
        #print(simqueue.size())
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue() 
print(hotline(["babu","Devi","Subha","kene","able","Jeffery"],7)

