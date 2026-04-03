
#2
input="aaabbcccc"

def compress(string):
    var=''
    counter=0
    for each in string:
        if(each=="a"):
           var+=each
           counter+=1
    print(var,counter)
    counter=0
    var=''
    for each in string:
        if(each=="b"):
           var+=each
           counter+=1
    print(var,counter)
    counter=0
    var=''
    for each in string:
        if(each=="c"):
           var+=each
           counter+=1
    print(var,counter)
    counter=0




# compress(input) 0.5


#5 0.5
s = "aabbccdq"
def repitItem(string):
    for each in string:
       if each==each:
        continue
       else:
          each!=each
          break
    return each

ans=repitItem(s)
print(ans)



#3
num=[1,2,3,4]

def matrix(myList):
   i=1
   maxValue=[]
   for each in myList:
     i*=each
     sum=i
#    print(sum)
     
   for item in myList:
       maxValue.append(sum/item)
   print(maxValue)
   
# matrix(num) 1


#1
s = "xxaxbcxabjjjcbdq"
def max (item):
    myList=[]
    counter=0
    for each in item:
        if each not in myList:
            myList.append(each)
            counter+=1
    print(counter)

max(s) 



