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