nums=[10,20,30,40,50]

def queuenum(ListQueue):
 queue=[]
 myQueue=[]
 for each in ListQueue:
  queue.append(each)
 for eachnum in ListQueue:
  var=queue.pop()
  myQueue.append(var)
 print(myQueue)

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

def sumnum(sumList,sumValue):
  queue=[]
  index=sumValue-1
  for each in sumList:
    if(index>-1):
      queue.append(sumList[index])
      index-=1
#   print(queue)
  for eachnum in sumList:
    if(eachnum not in queue):
      queue.append(eachnum)
  print(queue)
  


# sumnum([1,2,3,4,5,6,7,8,9,10],4)


def findvalue(sumList,target):

  index=target
  coventer=0 # 0
  
  # for each in sumList:
  #  coventer1=0 # c1=0 c=0 each=1
  #  for sumEach in sumList:
  #   # print(sumEach,each) 
  #   if(each+sumEach==index):
  #    coventer1+=1
  #    coventer+=1
     
  # print(coventer1,coventer)
  outerCounter = 0
  while outerCounter < len(sumList):
    # print(outerCounter, sumList[outerCounter])
    innerCounter = outerCounter+1
    while innerCounter < len(sumList):
      # print(outerCounter, "outerCounter", "      ", innerCounter, "innerCounter", sumList[innerCounter], sumList[outerCounter])
      if(sumList[outerCounter] + sumList[innerCounter] == target):
        # print(innerCounter, outerCounter)
        return [innerCounter, outerCounter]

      innerCounter+=1
    outerCounter+=1

    
    
    
# ans=findvalue([1,2,3,4,5,6,7],8)
# print(ans)


def sum(a): # a=2
  # print(a)
  if(a == 30): # base condition
    return a
  else:
    return sum(a + 3) # a=10

# recursion a function calling itself is called as recursion
ans = sum(3)
# print(ans)



def sumList(arry):
  # n=len(arry)
  # myFinalList=[]
  # for sumeach in range(n):
  #   total=0
  #   for each in range(sumeach,n):
  #    total+=arry[each]
     
  #   myFinalList.append(total)
  # return myFinalList
  total=0
  myList=[]
  for x in arry:
    total+=x
  # print(total)
  index = 0
  for y in arry:
    if(not(index == 0)):
      total-=arry[index-1]
    myList.append(total)

    # if(index == 0):
    #    myList.append(total)
    # else:
      
    #   myList.append(total)
    index+=1
   
  print(myList)
  
  
# ans=sumList([1,8,10,10])
# print(ans)








