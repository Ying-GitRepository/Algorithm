class Solution(object):
  def solve(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    length = len(array)
    if(length <= 0):
      return array 

    for i in range(length-1, 0, -1):
      max_index = i
      for j in range(i-1, -1, -1):
        if(array[j] > array[max_index]):
          max_index = j
      array[i], array[max_index] = array[max_index],array[i]
    return array
