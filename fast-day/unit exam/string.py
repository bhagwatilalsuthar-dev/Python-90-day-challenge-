

def palindrome(valuePalindrome):
    if(valuePalindrome==''):
        return"It's  palindrome"
    uppercase=valuePalindrome.upper()
    reversvalue=uppercase[::-1]
    if(uppercase==reversvalue):        
        return "It's   palindrome"

    else:
        return "not palindrome"

# finalAns=palindrome("mada")
# print(finalAns)


def valueOfpalindrome(string):
    if(string==""):
        return "is palindrome"
    uppercase=string.upper()
    rev=''
    for chackpalindrome in uppercase:
        rev=chackpalindrome+rev
        # print(rev,"rev", chackpalindrome,rev)
    if(uppercase==rev):
        return "is palindrome"
    else:
        return "not palindrome"
    
ans=valueOfpalindrome('mada')
# print(ans)


def BalanceBracket(Bracket):
    counter=0
    for EachBalnce in Bracket:
        if EachBalnce=='('or EachBalnce=='['or EachBalnce=='{':
            counter=counter+1
        if EachBalnce==')'or EachBalnce==']'or EachBalnce=='}':
            counter=counter-1
    if counter==0:
      return 'Balance'
    else:
        return 'not balance'
    
result=BalanceBracket('((([[[{{{}}]]])))')
print(result)

