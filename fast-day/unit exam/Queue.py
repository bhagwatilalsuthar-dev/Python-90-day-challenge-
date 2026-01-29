# nums=[10,20,30,40,50]

# def queuenum(ListQueue):
#  queue=[]
#  myQueue=[]
#  for each in ListQueue:
#   queue.append(each)
#  for eachnum in ListQueue:
#   var=queue.pop()
#   myQueue.append(var)
#  print(myQueue)

# queuenum(nums)

def sumList(x,y):
    queue=[]
    index=y-1
    for each in x:
     if(index>-1):
        queue.append(x[index])
        index-=1
    for eachnum in x:
     if(eachnum not in queue):
       queue.append(eachnum)
    print(queue)
     

sumList([10,20,30,40,50],3
)