def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    newS = ""
    
    for c in s:
        if c.isalnum():
            newS += c.lower()
    return newS == newS[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
