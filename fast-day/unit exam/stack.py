


def reverseFinder(revStr):
    stack=[]
    var=''
    for eachnam in revStr:
        stack.append(eachnam)
    for rev in revStr:
     var+=stack.pop()
    print(var)
   

# reverseFinder('hello')




def isPalindrome(palstr):
    stack=[]
    for palItem in palstr:
      stack.append(palItem)
    for revItem in palstr:
       if(stack.pop()==revItem):
            continue
       else:
          return'not palindrome'
    return'palindrome'
# print(isPalindrome('madm'))




elements = [1,2,3,4]
def revStack(revList):
    stack = []

    # push elements into stack
    for x in revList:
        stack.append(x)

    # pop elements to reverse
    while stack:
        print(stack.pop(), end=" ")
# revStack(elements)




# 1 stack to string 
stack=['a','b','c']
# print(''.join(stack))


# 2 remove all 2 in List
# stack=[1,2,3,4,2,4]
# for x in stack:
#    if(x!=2):
    #   print(x)


# 3 isPalindrome
s='madam'
# print(s==s[::-1])




def balanceBracket(value):
   stack=[]
   for each in value:
      if(each=="(" or each=="[" or each=="{"):
         stack.append(each)
         print(stack)
      else:
         stack.pop()==value
         return "yes"
   return "no"
ans=balanceBracket("((([))")
print(ans)


