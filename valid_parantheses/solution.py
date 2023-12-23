def isValid(s: str) -> bool:
    stack = []
    closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
    
    for c in s: # check each character in input string
        if c in closeToOpen: # check if character is closing parantheses (we look at the keys in our dictionary)
            if stack and stack[-1] == closeToOpen[c]: # make sure stack is not empty AND the value at the end is the matching open parantheses
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    
    return True if not stack else False


print(isValid("()[]{}")) 
print(isValid("[()]"))      


