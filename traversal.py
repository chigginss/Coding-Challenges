def num_of_paths_to_dest(n):
  # input: n - a positive integer representing the grid size.
  # output: number of valid paths from (0,0) to (n-1,n-1).
  # create a 2D array to save values
  memory = [0][0]
  
  # initialize with -1 and then add
  for i in range(0, n-1):
    for j in range(0, n-1):
      memory[i][j] = -1
      
  return paths_to_square(n-1, n-1, memory)

def paths_to_square(i, j, memory):
  if (i < 0 or j < 0):
    return 0
  elif (i < j):
    memory[i][j] = 0
  elif (i == 0 and j == 0):
    memory[i][j] = 1
  else: 
    memory[i][j] = paths_to_square(i,j - 1, memory) + paths_to_square(i - 1, j, memory)
  
  return memory[i][j]