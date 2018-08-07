""" Problems that involve string manipulation 

Are two strings anagrams, can you change one letter and have the same strings, 
how many characters do you have to delete to have the same strings

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

################################################################################

# most complicated: How many deletions 