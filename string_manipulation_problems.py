""" Problems that involve string manipulation 

Are two strings anagrams, can you change one letter and have the same strings, 
how many characters do you have to delete to have the same strings

Problems from Cracking the Coding Interview, Pramp and Hackbright 

"""

# simple: Are two strings anagrams of each other?

# psuedocode: order doesn't matter here. The main concept is that two strings 
# need to have the same amount of the same characters

def is_anagram(str1, str2):
    
    if sorted(str1) != sorted(str2):
        return False

    return True

# this is assuming strings are not case sensitive 
# runtime is 0(ab) because the sorted function 

#second solution 
#count how many letters and then compare counts / letters
def is_anagram(str1, str2):

    new_dict = {}

    for item in str1:
        if item not in new_dict:
            new_dict[item] = 1
        else:
            new_dict[item] += 1

    for item in str2:
        if item not in new_dict:
            return False
        else:
            new_dict[item] -= 1

    counts = new_dict.values()

    for item in counts:
        if item > 0:
            return False
        else:
            return True

################################################################################

# more complicated: One Edit Away 

# given two strings, need to find if you can change, add, or delete one letter to make strings equal
# first check length of both strings. If length is equal, we only need to worry about changing a letter
# if unequal, we need to check addition or deleting 
# only iterate through the longer string for faster runtime 

def one_edit_away(str1, str2):

    if len(str1) - len(str2) >= 2:
        return False
    elif len(str2) - len(str1) >= 2:
        return False
    else:
        if len(str1) > len(str2):
            count1 = 0
            for i in range(len(str1)):
                if str1[i] not in str2:
                    count += 1 
            if count > 1:
                return False
            else:
                return True
        elif len(str2) > len(str1):
            count2 = 0
            for i in range(len(str2)):
                if str2[i] not in str1:
                    count2 += 1 
            if count2 > 1:
                return False
            else:
                return True
        elif len(str1) == len(str2):
            count3 = 0
            for i in range(len(str1)):
                if str1[i] not in str2:
                    count += 1 
            if count > 1:
                return False
            else:
                return True

# runtime = 0(n+n+n) = 0(n)

def one_away(str1, str2):
    """Given two strings, are they, at most, one edit away?"""

    # START SOLUTION

    # Strings length can only vary by, at most, one letter
    if abs(len(st1) - len(str2)) > 1:
        return False

    # Make sure w2 is the shorter string
    if len(str2) > len(str1):
        str1, str2 = str2, str1

    if (str1.length < str2.length)
        shorter = str1
        str1 = str2
        str2 = shorter

    # Keep track of number of wrong letters
    wrong = 0

    # Loop over w1 with i and over w2 with j
    i = j = 0

    while j < len(str2):

        if str1[i] != str2[j]:

            # We found a wrong letter
            wrong += 1
            if wrong > 1:
                return False

            # We'll move to the next char in the longer string.
            i += 1

            # If same length, move the next char in shorter.
            # Otherwise, don't move in shorter string --- this
            # will cover the case of a added letter.
            if len(str1) == len(str2):
                j += 1

        else:
            # Both letters match; move to next letter in both
            i += 1
            j += 1

    return True

################################################################################

# most complicated: How many deletions 

""" The solution above takes O(N⋅M) space since we save all previous values, but notice that opt(i,j) requires only opt(i-1,j), opt(i,j-1) and opt(i-1,j-1). 
Thus, by iterating first through 0 ≤ i ≤ str1Len, and then for every i calculating 0 ≤ j ≤ str2Len, we need only to save the values for the current i and the last i. 
This will reduce the space needed for the function. """

Pseudocode:

function deletionDistance(str1, str2):
    # make sure the length of str2 isn't
    # longer than the length of str1
    if (str1.length < str2.length)
        tmpStr = str1
        str1 = str2
        str2 = tmpStr

    str1Len = str1.length
    str2Len = str2.length
    prevMemo = new Array(str2Len  + 1)
    currMemo = new Array(str2Len  + 1)

    for i from 0 to str1Len:
        for j from 0 to str2Len:
            if (i == 0):
                currMemo[j] = j
            else if (j == 0):
                currMemo[j] = i
            else if (str1[i-1] == str2[j-1]):
                currMemo[j] = prevMemo[j-1]
            else:
                currMemo[j] = 1 + min(prevMemo[j], currMemo[j-1])

        prevMemo = currMemo
        currMemo = new Array(str2Len + 1);  
                                           
    return prevMemo[str2Len]

# Time Complexity: the time complexity stays the same, i.e. O(N⋅M), since we still run a nested loop with N⋅M iterations.
# Space Complexity: O(min(N,M)), as we only need to hold two rows of the double array.