def alphaNum(c):
    # Check if character is alphanumeric (A-Z, a-z, 0-9)
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or 
            ord('0') <= ord(c) <= ord('9'))

def isPalindrome(s):
    l, r = 0, len(s) - 1 # Pointers at the start and end of the string
    
    while l < r:
        # Move left pointer if current char is not alphanumeric
        while l < r and not alphaNum(s[l]):
            print(f"Ignoring non-alphanumeric character at start: {s[l]}")
            l += 1
        # Move right pointer if current char is not alphanumeric
        while r > l and not alphaNum(s[r]):
            print(f"Ignoring non-alphanumeric character at end: {s[r]}")
            r -= 1
        # Check if characters at pointers are equal (ignoring case)
        if s[l].lower() != s[r].lower():
            print(f"Characters at pointers don't match: {s[l]} != {s[r]}")
            print("String is NOT a palindrome!")
            return False
        l, r = l + 1, r - 1  # Move both pointers towards the center
    
    print("String is a palindrome")
    return True

# Test the function
print(isPalindrome("A man, a plan, a canal: Panamaa"))  # Expected output: True
