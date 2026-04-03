def SumTarget(value,Target):
    
    i=0
    j=len(value)-1
    while i<j:
        sumitem=value[i]+value[j]
        if sumitem==Target:
            return [i,j]
            
        elif sumitem>Target:
            j-=1
        elif sumitem<Target:
            i+=1
        
    return[-1,-1]
        
ans=SumTarget([1,2,3,4,5,6,7,8,9,10,11,12,13],24)
print(ans)


def Duplicates(array):
    i=0
    j=1
    for j in range(1,len(array)):
        if(array[i] !=array[j]):
            i+=1
            array[i]=array[j]
    return array[:i+1]
    
            
       
# ans=Duplicates([1,2,2,3,4,4,5,5,6,7])
# print(ans)

def non_zero(arrey):
    
    i=0
    j=0
    while j<len(arrey):
        if arrey[j]!=0:
            arrey[i]=arrey[j]
        elif arrey[j]==0:
            j+=1
    return arrey




ans=non_zero([1,0,2,0,3,4])
print(ans)



