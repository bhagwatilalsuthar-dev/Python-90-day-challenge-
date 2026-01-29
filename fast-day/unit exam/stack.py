


def reverseFinder(revStr):
    stack=[]
    var=''
    for eachnam in revStr:
        stack.append(eachnam)
    for rev in revStr:
     var+=stack.pop()
    print(var)
   

reverseFinder('hello')
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
revStack(elements)