

def palindrome(valuePalindrome):
    if(valuePalindrome==''):
        return"It's  palindrome"
    uppercase=valuePalindrome.upper()
    reversvalue=uppercase[::-1]
    if(uppercase==reversvalue):        
        return "It's   palindrome"

    else:
        return "not palindrome"

finalAns=palindrome("mada")
print(finalAns)


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
    
# ans=valueOfpalindrome('mada')
# print(ans)


def BalanceBracket(Bracket):
    i=0
    j=len(Bracket)-1
    if(len(Bracket) % 2 != 0):
        return False
    print("aage badna padega")
    myPairDict = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    while i < j:
        # print(i,j,Bracket[i], Bracket[j])
        # print( Bracket[i],Bracket[j], myPairDict[Bracket[i]],  )
        if( Bracket[j] != myPairDict[Bracket[i]] ):
        # if( (Bracket[i] == "(" and Bracket[j] != ")") or (Bracket[i] == "[" and Bracket[j] != "]") or(Bracket[i] == "{" and Bracket[j] != "}") ):
            # print(i,j)
            return False
        i+=1
        j-=1
    return True
    
    
result=BalanceBracket('({])')
print(result)

