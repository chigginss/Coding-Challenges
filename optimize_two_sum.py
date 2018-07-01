def find_pairs_with_given_difference(arr, k):
  # loop through arr to find a pair that arr[i] - arr[j] = k
  # return pairs in an array [arr[i], arr[j]] nested if more than one
 # result = []
  
  
  #for i in range(len(arr)):
    #for j in range(len(arr)):
      # if arr[j] - arr[i] == k:
         # result.append([arr[j], arr[i]])
          
  #return result
  
  result = []
  new_dict = {}
  
  for i in range(len(arr)):
    if k + arr[i] in arr:

       # new_dict[k + arr[i]] = 