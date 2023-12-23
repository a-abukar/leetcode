def isValid(s: str) -> bool:
    stack = []
    closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
    
    for c in s:  # check each character in input string
        print(f"Checking character: {c}")
        if c in closeToOpen:  # check if character is a closing parenthesis
            if stack and stack[-1] == closeToOpen[c]:  # check if stack's last item matches
                print(f"Match found for {c}, popping {stack[-1]} from stack")
                stack.pop()
            else:
                print(f"No match for {c}, returning False")
                return False
        else:
            print(f"{c} is an opening parenthesis, adding to stack")
            stack.append(c)
    
    print(f"Final stack: {stack}")
    return True if not stack else False

# Example usage
# print(isValid("()}]{}")) 
print(isValid("[()]")) 