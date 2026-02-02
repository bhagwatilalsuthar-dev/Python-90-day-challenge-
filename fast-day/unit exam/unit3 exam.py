nums=[
    [0,0,1,1],
    [0,1,1,1],
    [1,1,1,1]
]
def MaximumNumber(NumberOfList):
 myList=[]
 
 for eachnum in NumberOfList:
    total=0
    
    for each in eachnum:
        total+=each
    myList.append(total)
#  print(myList)
 highValue(myList)
def highValue(x):
   high=float('-inf')
   ans=None
   i=0
   for each in x:
      if high<each:
         high=each
         ans=i
         i+=1
   print(ans)
MaximumNumber(nums)