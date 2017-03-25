"""
validBraces( "(){}[]" ) => returns true
validBraces( "(}" ) => returns false
validBraces( "[(])" ) => returns false
validBraces( "([{}])" ) => returns true
'([}{])' - False
')(}{][' - False
"""

def validBraces(string):
    bracer = []
    pardict = {"{":"}", "[":"]", "(":")", "}":"{", "]":"[", ")":"("}
    for i in range(len(string)):
        if string[i] == "(" or string[i] == "[" or string[i] == "{":
            bracer.append(string[i])
        else:
            if len(bracer) == 0:
                return False
            elif pardict[string[i]] == bracer[len(bracer)-1]:
                del bracer[len(bracer)-1]
            else:
                return False
    if len(bracer) != 0:
        return False
    return True


print(validBraces('(){}[]'))
