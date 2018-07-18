"""palindrome"""

def is_palindrome(str):

    for i in range(0, len(str)/2):
        if str[i] != str[len(str)-i-1]
            return false


# second solution 

def is_palindrome(str):
    
    if str != reversed(str):
        return false