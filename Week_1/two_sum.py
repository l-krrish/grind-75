'''
Two Sum

Most Optimised Solution - Use a Hashmap

Complexity Analysis

Time complexity: O(n).
We traverse the list containing n elements only once. Each lookup in the table costs only O(1) time.

Space complexity: O(n).
The extra space required depends on the number of items stored in the hash table, which stores at most n elements.

'''

class Solution:
  def TwoSum(self, nums : List[int], target : int) -> List[int]:
    hashmap={}
    for i in range(len(nums)):
      complement=target-nums[i]
      if complement in hashmap:
        return [i,hashmap[complement]]
      hashmap[nums[i]]=i
    return []
