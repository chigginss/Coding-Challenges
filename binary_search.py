"""Binary Search"""

def binary_search(array, target):

    lower = 0
    upper = len(array)

    while lower < upper:
        guess = lower + (upper - lower) / 2
        val = array[guess]
        if target == val:
            return guess
        elif target > val:
            if lower == guess:
                break
            lower = guess
            elif target < val:
                upper = guess
