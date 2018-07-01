
"""Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and 
returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. 
Assume that the offset doesn’t equal to 0 (i.e. assume the array is shifted at least once) or to arr.length - 1 
(i.e. assume the shifted array isn’t fully reversed)."""
    

def shifted_arr_search(shiftArr, num):
    # loop through shiftArr using range
    # if num is in shiftArr
    # dictionary key[num] = index
    # return -1 
    #new_dict = {}
    
    for i in range(len(shiftArr)):
        new_dict[shiftArr[i]] = i
    #{9:0, 12:1, 17:2, 2:3...}
    
    if num in new_dict:
        return new_dict[num]
    else:
        return -1
      